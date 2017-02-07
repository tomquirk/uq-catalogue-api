from scrape import Catalogue
from db import Db


class Migrate:
    """
    Builds database (full wipe, no diff)
    """
    def __init__(self):
        self._db = Db()
        self._db.connect('uq_catalogue', 'tomquirk', '', 'localhost')
        self._prerequisite_set_count = 0

        self._blacklist = ['COMP1500']  # temporary, should be moved to scrape.py

    def reset(self):
        """
        Clears DB, truncating each table in order of dependency
        :return: None
        """
        queries = [
            'DELETE from plan_course_list',
            'DELETE from course_semester_offering',
            'DELETE from course', 'DELETE from plan',
            'DELETE from program'
        ]

        for sql in queries:
            self._db.commit(sql)

    def get_state(self):
        """
        Returns boolean based on existence of plan code in database (a 'cheap' diff)
        :param plan_code: program plan code
        :return:
        """
        state = {
            'programs': [],
            'plans': [],
            'courses': []
        }

        data = self._db.select('SELECT * FROM plan')

        for row in data:
            state['plans'].append(row[0])

        data = self._db.select('SELECT * FROM program')

        for row in data:
            state['programs'].append(row[0])

        data = self._db.select('SELECT * FROM course')

        for row in data:
            state['courses'].append(row[0])

        return state

    def init_catalogue(self):
        """
        Builds and returns course
        :return: None
        """
        state = self.get_state()
        file = open('backup/catalogue.txt', 'r')
        catalogue = file.read()
        if len(catalogue) == 0:
            catalogue = Catalogue.scrape_catalogue(state)
        else:
            catalogue = eval(catalogue)

        print("************* INITIALIZED MIGRATIONS *************")

        for program in catalogue['program_list']:
            if program['program_code'] not in state['programs']:
                self.add_program(program)

        for course in catalogue['course_list']:
            self.add_course(course)

        for plan in catalogue['plan_list']:
            self.add_plan(plan)

        print("************* MIGRATIONS COMPLETE *************")

    def add_program(self, program):
        """

        :param program: Dictionary
        :return:
        """
        sql = """INSERT INTO program
              (program_code, title, level, abbreviation, duration_years, units)
              VALUES ('%s', '%s', '%s', '%s', '%d', '%d')
              """ % (program['program_code'], program['title'],
               program['level'], program['abbreviation'],
               program['durationYears'], program['units'])

        self._db.commit(sql)

    def add_plan(self, plan):
        """

        :param plan: Dictionary
        :return:
        """
        sql = """INSERT INTO plan
              (plan_code, program_code, title)
              VALUES ('%s', '%s', '%s')
              """ % (plan['plan_code'], plan['program_code'],
               plan['title'])


        self._db.commit(sql)

        for course_code in plan['course_list']:
            # if course_code in plan['required_course_list']:
            #     isRequired = 1
            isRequired = 0
            self.add_plan_course_list(plan['plan_code'], course_code, isRequired)

    def add_course(self, course):
        """

        :param course: Dictionary
        :return:
        """
        print("\nADDING: " + course['course_code'] + " to Course")

        sql = """INSERT INTO course
              (course_code, title, description, raw_prerequisites,
              units, course_profile_id) VALUES ('%s', '%s', '%s', '%s', '%d', '%s')
              """ % (course['course_code'], course['title'],
               course['description'].replace("'", "''"), course['raw_prereqs'],
               course['units'], course['course_profile_id'])


        self._db.commit(sql)
        for semester_offering in course['semester_offerings']:
            self.add_course_semester_offering(course['course_code'],
                                              semester_offering)
        print("\tCOMPLETE: " + course['course_code'])

    def add_course_semester_offering(self, course_code, semester_offering):
        """

        :param course_code:
        :param semester_offering:
        :return:
        """

        sql = """INSERT INTO course_semester_offering (course_code, semester_offering)
              VALUES ('%s', '%s')""" % (course_code, semester_offering)

        self._db.commit(sql)

    def add_plan_course_list(self, plan_code, course_code, required):
        """

        :param plan_code:
        :param course_code:
        :return:
        """
        sql = """INSERT INTO plan_course_list (course_code, plan_code, required)
              VALUES ('%s', '%s', '%d')""" % (course_code, plan_code, required)

        self._db.commit(sql)

if __name__ == "__main__":
    migration = Migrate()
    migration.reset()
    migration.init_catalogue()
