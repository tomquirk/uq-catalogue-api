"""
Migrate
"""
import src.database as database
import src.scrape as scrape
import src.settings as settings

from src.logger import get_logger

_LOG = get_logger("pipeline")


class Pipeline:
    """
    Utility class for ETL pipeline
    """

    def __init__(self):
        self._db = database.Db(detailed=False)
        self._db.connect(
            settings.DATABASE["NAME"],
            settings.DATABASE["USER"],
            settings.DATABASE["PASSWORD"],
            settings.DATABASE["HOST"],
        )

    def reset(self):
        """
        Clears DB, truncating each table in order of dependency
        :return: None
        """
        check = input(
            "Wipe database and start over (WARNING: this will remove all existing data in the database)? [Y/n] "
        )
        if check.lower() != "y":
            return

        queries = [
            "DELETE from course_to_plan",
            "DELETE from course_to_program",
            "DELETE from incompatible_courses",
            "DELETE from course_assessment",
            "DELETE from course",
            "DELETE from plan",
            "DELETE from program",
        ]

        for sql in queries:
            self._db.commit(sql)

    def run(self):
        """
        Runs the pipeline
        :return: None
        """
        _LOG.info("Pipeline init")
        program_list = scrape.catalogue()

        for program_code in program_list:
            program = self.get_or_add_program(program_code)
            if not program:
                continue

            program_course_list = scrape.program_course_list(program_code)
            self.add_courses_to_program(program_code, program_course_list)

            for plan in program_course_list:
                plan_code = plan["plan_code"]
                plan = self.get_or_add_plan(plan_code, plan["title"])
                if not plan:
                    continue

                plan_rules = scrape.plan_rules(plan_code)
                plan_course_list = plan_rules.get("course_list", [])
                self.add_courses_to_plan(plan["plan_code"], plan_course_list)

        _LOG.info("Pipeline finished")

    def get_or_add_program(self, program_code):
        """

        :param program_code: String, 4 digit code of desired program
        :return:
        """
        _LOG.info(f"Getting program: {program_code}")
        stmt = """
            SELECT *
            FROM program
            WHERE program_code = (%s)
            """
        res = self._db.select(stmt, data=(program_code,))

        if res:
            program_data = {
                "program_code": res[0][0],
                "title": res[0][1],
                "level": res[0][2],
                "abbreviation": res[0][3],
                "durationYears": res[0][4],
                "units": res[0][5],
            }

            return program_data

        program = scrape.program(program_code)

        if program is None:
            return None

        if res:
            return program

        stmt = """
              INSERT INTO program
              VALUES (%s, %s, %s, %s, %s, %s)
              """

        self._db.commit(
            stmt,
            data=(
                program_code,
                program["title"],
                program["level"],
                program["abbreviation"],
                program["durationYears"],
                program["units"],
            ),
        )

        return program

    def add_courses_to_program(self, program_code, courses):
        """

        :param program_code: String, 4 digit code of desired program
        :return:
        """
        for course_code in courses:
            course = self.get_or_add_course(course_code)
            if course is None:
                continue

            sql = """
                  INSERT INTO course_to_program 
                  VALUES (%s, %s)
                  ON CONFLICT DO NOTHING
                  """

            self._db.commit(sql, data=(course_code, program_code))

        return courses

    def get_or_add_plan(self, plan_code, plan_title):
        """

        :param plan_code: String, 5 letter plan key followed by 4 digit
                            program code (e.g. SOFTWX2342)
        :param plan_title: String, plan title
        :return:
        """
        _LOG.info(f"Getting plan: {plan_code}")
        sql = (
            """
            SELECT *
            FROM plan
            WHERE plan_code = (%s)
            """
            % plan_code
        )
        res = self._db.select(sql, data=(plan_code,))

        if res:
            {"plan_code": res[0][0], "title": res[0][2], "program_code": res[0][1]},

        plan = scrape.plan(plan_code)

        if plan is None:
            return

        sql = """
              INSERT INTO plan
              VALUES (%s, %s, %s)
              """

        self._db.commit(sql, (plan["plan_code"], plan["program_code"], plan_title))

        return plan

    def add_courses_to_plan(self, plan_code, courses):
        """

        :param plan_code: String, 5 letter plan key followed by 4 digit
                            program code (e.g. SOFTWX2342)
        :param courses: List, containing Strings, all course codes
                            (e.g. CSSE1001)
        :return: None
        """
        for course_code in courses:
            course = self.get_or_add_course(course_code)
            if course is None:
                continue

            sql = """
                INSERT INTO course_to_plan
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
                """

            self._db.commit(sql, data=(course_code, plan_code))

    def get_or_add_course(self, course_code):
        """

        :param course_code: String, 4 letters followed by 4 digits
                                (e.g. MATH1051)
        :return:
        """
        _LOG.info(f"Getting course: {course_code}")

        # Check for db entry for course. Don't scrape it if yes
        if len(course_code) != 8:
            return

        sql = """
            SELECT course_code, course_profile_id
            FROM course
            WHERE course_code = (%s)
            """

        res = self._db.select(sql, data=(course_code,))

        if res:
            profile_id = res[0][1]
            if profile_id:
                self.refresh_course_profile(course_code, profile_id)
            # TODO should return a course object here instead of nothing
            return True

        course = scrape.course(course_code)

        if course is None:
            return

        # flag course as invalid in DB
        if course is False:
            sql = """
              INSERT INTO course
              (course_code, not_offered)
              VALUES (%s, %s)
              """

            self._db.commit(sql, data=(course_code, True))
            return {"course_code": course_code}

        title = course.get("title", "")
        if title:
            title = title.replace("'", "''")

        description = course.get("description", "")
        if description:
            description = description.replace("'", "''")

        raw_prereqs = course.get("raw_prereqs", "")
        if raw_prereqs:
            raw_prereqs = raw_prereqs.replace("'", "''")

        sql = """
              INSERT INTO course
              VALUES (%s, %s, %s, %s, 
              %s, %s, %s, %s, %s, %s)
              """

        self._db.commit(
            sql,
            data=(
                course["course_code"],
                title,
                description,
                raw_prereqs,
                course["units"],
                course["course_profile_id"],
                course["semester_offerings"][0],
                course["semester_offerings"][1],
                course["semester_offerings"][2],
                True,
            ),
        )

        self.add_incompatible_courses(course_code, course["incompatible_courses"])

        # TODO return an actual course object here
        return {"course_code": course_code}

    def refresh_course_profile(self, course_code, course_profile_id):
        _LOG.info(f"Refreshing course profile: {course_code}")
        sql = """
            DELETE FROM course_assessment
            WHERE course_code = (%s)
            """
        self._db.commit(sql, data=(course_code,))

        course_profile = scrape.course_profile(course_code, course_profile_id)

        if not course_profile:
            return

        for assessment in course_profile:
            due_date_str = None
            if assessment.get("due_date"):
                due_date_str = assessment.get("due_date").isoformat()

            sql = """
                INSERT INTO course_assessment (course_code, assessment_name, due_date, weighting, learning_obj)
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """

            self._db.commit(
                sql,
                data=(
                    assessment["course_code"],
                    assessment["name"].replace("'", "''"),
                    due_date_str,
                    assessment["weighting"],
                    assessment["learning_obj"],
                ),
            )

        return course_profile

    def add_incompatible_courses(self, course_code, incompatible_courses):
        """

        :param course_code: String, course code of parent
        :param incompatible_courses: List, course code/s as Strings
        :return:
        """
        _LOG.info(f"Flagging incompatible courses: {course_code} <=/=> {str(incompatible_courses)}")
        last_course_code_prefix = None

        for i_course_code in incompatible_courses:
            if len(i_course_code) == 8:
                last_course_code_prefix = i_course_code[:4]
            if len(i_course_code) == 4:
                i_course_code = f"{last_course_code_prefix}i_course_code"
            # Ensure all courses are added to `course` table
            course = self.get_or_add_course(i_course_code)
            if course is None:
                continue

            sql = """
                SELECT course_code
                FROM incompatible_courses
                WHERE course_code = (%s)
                AND incompatible_course_code = (%s)
                """

            res = self._db.select(sql, data=(course_code, i_course_code))
            if res:
                continue

            sql = """
                  INSERT INTO incompatible_courses
                  VALUES (%s, %s)
                  """

            self._db.commit(sql, data=(course_code, i_course_code))


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.reset()
    pipeline.run()
