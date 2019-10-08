# from src.pipeline import Pipeline
# import src.database as database
# import src.settings as settings

# courses_with_summer_sem = ['ADVT7508', 'AGRC2031', 'AGRC3602', 'AGRC4617', 'AGRC6642', 'ANCH2900', 'ANTH1030', 'ANTH1101X', 'ANTH2208', 'ARCH7012', 'ARCH7022', 'ARCH7032', 'ARCH7042', 'ARCS2003', 'ARTT3200', 'BIOC6006', 'BIOC6014', 'BIOC7003', 'BIOC7009', 'BIOC7010', 'BIOC7011', 'BIOC7014', 'BIOC7018', 'BIOC7021', 'BIOC7025', 'BIOC8000', 'BIOL3210', 'BIOL3232', 'BIOL7005', 'BIOL7232', 'BIOL8001', 'BIOT3007', 'BIOT4002', 'BIOT4020', 'BIOT4039', 'BIOT4070', 'BIOT6010', 'BIOT6011', 'BIOT6014', 'BIOT6015', 'BIOT7003', 'BIOT7004', 'BIOT7010', 'BIOT7011', 'BIOT7012', 'BIOT7014', 'BIOT7015', 'BIOT7024', 'BIOT7029', 'BIOT7034', 'BIOT7035', 'BIOT8000', 'BIOT8001', 'BIOT8002', 'BIOT8007', 'BIOT8010', 'BISM7807', 'CHEM1200', 'COMP4000', 'COMP7000', 'COMP7860', 'COMU3801', 'CONS7024', 'CRIM1019', 'DECO3000', 'DECO7000', 'DRAM3104', 'ECON1010', 'ECON1020', 'ECON1310', 'ECON2070', 'ECON2200', 'ECON2540', 'ECON3220', 'ECON7070', 'ECON7530', 'ECON7540', 'ECON7740', 'ECON7930', 'EDUC7026', 'EDUC7027', 'EDUC7570', 'EDUC7585', 'EDUC7590', 'EDUC7910', 'ELEC7300', 'ENGG7300', 'ENGL3020', 'ENGY7113', 'ENGY7116', 'ENVM3102', 'ENVM3104', 'ENVM7109', 'ENVM7124', 'ENVM7129', 'ENVM7133', 'ERTH7301', 'EVNT3003', 'EXCH1031', 'EXMD4701', 'EXMD4702', 'EXMD7315', 'EXMD7316', 'FINM2401', 'FINM3400', 'FINM7805', 'FREN1020', 'GEOM7005', 'GEOS3400', 'GEOS7400', 'HLTH7308', 'HMST3001', 'HMST4314', 'HMST4925', 'HOSP2001', 'HOSP7051', 'JAPN1013', 'JAPN1023', 'JOUR3801', 'KORN1010', 'KORN1011', 'LAWS4114', 'LAWS5179', 'LAWS5225', 'LAWS5229', 'LAWS5233', 'LAWS7723', 'LAWS7825', 'LAWS7944', 'LTCS2023', 'MATH1051', 'MATH1052', 'MATH2000', 'MATH2001', 'MATH7000', 'MATH7014', 'MATH7016', 'MATH7052', 'MGTS1982', 'MGTS7603', 'MGTS7803', 'MGTS7810', 'MGTS7906', 'MKTG1501', 'MKTG7806', 'MOLI7105', 'MOLI7204', 'MUSC3240', 'MUSC4270', 'MUSC7710', 'MUSC7900', 'NURS3002', 'NURS7106', 'NURS7110', 'NUTR1023', 'OHSS4012', 'PHTY4402', 'PHTY4403', 'PHTY4404', 'PHTY4405', 'PHTY4409', 'PHTY7802', 'PHTY7803', 'PHTY7825', 'PHTY7881', 'PHTY7882', 'PHTY7883', 'PHTY7884', 'PHTY7888', 'PLAN4130', 'PLAN7130', 'PLAN7430', 'PLNT3012', 'POLS3802', 'POLS7108', 'POLS7120', 'POLS7125', 'POLS7207', 'POLS7220', 'POLS7521', 'POLS7704', 'PSYC1030', 'PSYC2991', 'PSYC2992', 'PSYC7524', 'PSYC7534', 'PSYC7544', 'PSYC7554', 'PSYC7745', 'PSYC7755', 'PSYC7810', 'PSYC7820', 'PSYC7830', 'PSYC7840', 'PSYC7850', 'PSYC7860', 'PSYC8320', 'PSYC8330', 'PSYC8340', 'PUBH7026', 'PUBH7031', 'PUBH7117', 'PUBH7124', 'PUBH7900', 'RELN9000', 'RELN9001', 'SCIE3050', 'SCIE3221', 'SCIE3226', 'SCIE3230', 'SCIE3241', 'SCIE3251', 'SCIE3255', 'SCIE3260', 'SCIE3261', 'SCIE3271', 'SOCY1050', 'SPCH7809', 'STAT1201', 'TIMS7811', 'TOUR2001', 'TOUR3003', 'TOUR3008', 'TOUR7032', 'VREX1031', 'VREX1035', 'WATR7200', 'WATR7800', 'WRIT1999', 'WRIT7045']

# # for course_code in courses_with_summer_sem:
# #   ID_query = "SELECT course_profile_id FROM course_profile WHERE course_code = '%s';" % course_code

# #   profileID = database.select(ID_query)
# #   if len(profileID) != 0:
# #     profileID = profileID[0][0]
# #   else:
# #     continue
  
# #   sql1 = "DELETE FROM course_profile WHERE course_code = '%s';" % (course_code)
  
# #   sql2 = "DELETE FROM course_assessment WHERE course_profile_id = '%s';" % (profileID)
# #   database.commit(sql2)
# #   database.commit(sql1)
# #   print('done cunt')
# pipe = Pipeline()


"""
Migrate
"""
import re

import src.database as database
import src.scrape as scrape
import src.settings as settings
from src.scrape.course_profile import format_date

from src.logger import get_logger
from src.util import is_course_code, is_plan_code, is_program_code

_LOG = get_logger("pipeline")


def to_plan(sql_res):
    return {"plan_code": sql_res[0], "title": sql_res[2], "program_code": sql_res[1]}


class Pipeline:
    """
    Utility class for ETL pipeline
    """

    def __init__(self):
        self._db = database.Db()
        self._db.connect(
            settings.DATABASE["NAME"],
            settings.DATABASE["USER"],
            settings.DATABASE["PASSWORD"],
            settings.DATABASE["HOST"],
        )

    def run(self):
        """
        Runs the pipeline
        :return: None
        """
        _LOG.info("pipeline init")

        courses_with_fucked_weightings = ['FINM7401', 'CHEE2010', 'FINM1415', 'ECON3210', 'ECON6300', 'ECON3520', 'HUMN1201', 'ANCH1240', 'ANCH2290', 'GREK2120', 'GREK2230', 'ARTT2200', 'DRAM2200', 'COSC2500', 'MATH3104', 'MUSC2510', 'MUSC2710', 'MUSC2630', 'PHIL2090', 'SCIE1000', 'SCIE1100', 'SCIE2011', 'SCIE1200', 'BIOL2006', 'BIOL2106', 'BIOL2202', 'BIOL2902', 'BIOL6402', 'BIOL6403', 'BIOL6501', 'BIOL6502', 'BIOL6503', 'BIOC6511', 'BIOC6512', 'AGRC6001', 'BIOM1051', 'BIOM1050', 'BIOL1040', 'BIOC6017', 'BIOC3000', 'MICR2000', 'BIOC3003', 'BIOC3005', 'BIOC3006', 'BIOL3004', 'BIOL2015', 'BIOL2203', 'BIOL2205', 'BINF7000', 'BIOL3014', 'MICR3003', 'BIOM2222', 'BIOM6502', 'BIOM6503', 'BIOM2012', 'ANAT1005', 'ANAT1018', 'ANAT1020', 'BIOM2020', 'SCIE3220', 'BIOM3002', 'BIOM3014', 'BIOM3401', 'BIOT3002', 'CHEM3010', 'CHEM3016', 'CHEM6511', 'CHEM6512', 'GEOM1000', 'COSC3000', 'GEOM7004', 'GEOM3005', 'PHYS3071', 'SCIE3250', 'PHYS1001', 'PHYS1002', 'PHYS2020', 'PHYS2041', 'PHYS2055', 'PHYS3020', 'PHYS7250', 'PHYS3051', 'PHYS7270', 'PHYS3080', 'AGRC3042', 'VETS3040', 'ARCS3010', 'COSC7502', 'COSC3500', 'CSSE7201', 'CSSE2010', 'CSSE7231', 'DECO7250', 'DECO2500', 'STAT3500', 'AGRC3027', 'LAND3007', 'ABTS1000', 'MUSC2810', 'ARCS2070', 'COMU1002', 'WRIT1001', 'ECON2420', 'FREN3113', 'GEND1010', 'ENVM7202', 'POLS3801', 'COMU3110', 'MUSC3160', 'MUSC3840', 'MUSC3850', 'MUSC3890', 'POLS1501', 'MUSC2000', 'PSYC3020', 'PSYC3102', 'PSYC3202', 'SOCY3200', 'HPRM1000', 'HUMN2500', 'SOSC6040', 'ANTH6008', 'ARCA6008', 'SLAT7806', 'LTCS6000', 'CHIN6364', 'CHIN6340', 'CHIN6350', 'CRIM6008', 'KORN6364', 'MUSC4231', 'PSYC4060', 'PSYC4071', 'PSYC4091', 'PSYC4221', 'SOCY6008', 'HMST6001', 'HMST6002', 'EDUC3099', 'EDUC4703', 'EDUC4615', 'BIOM3200', 'BIOM6192', 'BIOM6193', 'CHEE3301', 'DECO3801', 'COMP7308', 'COMP3301', 'DECO7350', 'DECO3500', 'CHEE3002', 'CHEE2003', 'CHEE4034', 'ENGY4000', 'MECH2300', 'BIOT6121', 'BIOT6122', 'BIOT6123', 'PHYL1007', 'ANAT2000', 'ANAT2029', 'EXMD2362', 'EXMD7382', 'EXMD2382', 'EXMD3372', 'EXMD4740', 'EXMD7741', 'EXMD4741', 'DECO7110', 'DECO1100', 'DECO7220', 'DECO2200', 'CSSE7306', 'CSSE3006', 'DECO7385', 'DECO3850', 'ENGG1600', 'COMP2000', 'COMP3001', 'COMP4001', 'DECO2000', 'DECO4000', 'CRIM4103', 'CRIM4104', 'DENT1050', 'BIOM1052', 'DENT2050', 'DENT3060', 'DENT3070', 'DENT3061', 'DENT3071', 'DENT4060', 'DENT4070', 'DENT4061', 'DENT4071', 'DENT5100', 'DENT5200', 'EDUC2703', 'EDUC3701', 'EDUC3702', 'EDUC4706', 'ENGG1200', 'ENGG1211', 'ENGG1100', 'CHEE3020', 'CHEE3005', 'CHEE3007', 'CHEE4060', 'CHEE7103', 'CHEE4001', 'MINE2201', 'MINE3212', 'MINE3219', 'CHEE4006', 'MINE4205', 'CHEE4007', 'CHEE4026', 'CHEE4027', 'MINE4204', 'MECH3301', 'MINE3208', 'CIVL2360', 'CIVL3420', 'CIVL4250', 'METR2800', 'ENGG2800', 'ELEC7401', 'ELEC3400', 'ENGG3800', 'ENGG4801', 'ENGG4802', 'ENGG4805', 'CSSE7411', 'CSSE4011', 'ELEC4001', 'ELEC7403', 'ELEC4403', 'MECH3600', 'ENGG7800', 'ENGG4800', 'MECH2210', 'MECH3200', 'MECH3410', 'MECH4501', 'MECH4552', 'AERO4470', 'MECH3250', 'MECH3750', 'PHYS2082', 'METR4810', 'METR4900', 'METR4901', 'DECO3800', 'DECO7450', 'DECO4500', 'ENGG7282', 'CHEE7112', 'WATR7109', 'ENGG7301', 'COMP7001', 'DECO7001', 'ANIM1006', 'AGRC6650', 'HLTH3001', 'EDUC3004', 'EDUC3006', 'EDUC4005', 'COMP6804', 'COMP6801', 'COMP6803', 'SOSC6100', 'LAWS5180', 'BIOM1060', 'MIDW1101', 'MIDW1103', 'NUMW1102', 'MIDW1104', 'MIDW1105', 'MIDW2102', 'MIDW2108', 'MIDW2103', 'MIDW2106', 'MIDW3001', 'MIDW3102', 'MIDW3104', 'MUSC3231', 'MUSC1150', 'MUSC1100', 'MUSC1110', 'MUSC2100', 'MUSC2110', 'MUSC3180', 'MUSC3190', 'MUSC3280', 'MUSC3290', 'NURS1101', 'NURS1103', 'NURS1104', 'NURS1105', 'NURS2103', 'NURS2104', 'NURS2105', 'NURS2106', 'NURS3001', 'NURS3102', 'NURS3104', 'OCTY1102', 'OCTY7809', 'OCTY1105', 'OCTY1205', 'OCTY7826', 'OCTY7828', 'HRSS7101', 'HRSS3101', 'OCTY3103', 'OCTY3208', 'OCTY4104', 'HRSS7200', 'HRSS4210', 'OCTY4206', 'PHRM1011', 'PHRM1012', 'PHRM2011', 'PHRM3011', 'PHRM3012', 'PHRM4011', 'PHRM4061', 'PHRM4062', 'PHRM4080', 'ANAT2012', 'PHTY2101', 'PHTY4401', 'VETS1030', 'VETS2032', 'FOOD3601', 'AGRC6005', 'SWSP1033', 'SWSP2077', 'SWSP2088', 'SWSP3028', 'SWSP3029', 'SWSP4088', 'SWSP4266', 'SWSP7266', 'SWSP7366', 'SWSP7165', 'SWSP7155', 'SWSP3155', 'SWSP3022', 'SWSP3027', 'SWSP3076', 'SWSP4181', 'SWSP4182', 'SWSP4183', 'ANAT1022', 'SPCH2106', 'ANAT2005', 'SPCH2203', 'SPCH3107', 'SPCH3205', 'SPCH4105', 'SPCH4202', 'SPCH4206', 'VETS1018', 'VETS1021', 'VETS1025', 'ANIM2501', 'VETS3010', 'VETS3024', 'VETS4010', 'VETS5012', 'VETS5020', 'VETS5024', 'VETS5028', 'VETS5029', 'VETS5030', 'VETS5016', 'VETS2001', 'VETS3044', 'VETS6621', 'VETS6622', 'ARCS2003', 'ARTT3200', 'BIOC7003', 'BIOC7010', 'BIOC7011', 'BIOC7021', 'BIOC8000', 'BIOT6014', 'BIOT6015', 'BIOT7014', 'BIOT7015', 'COMP7860', 'COMU3801', 'DRAM3104', 'ENVM3102', 'EXMD4701', 'EXMD4702', 'FINM2401', 'GEOM7005', 'HMST3001', 'HMST4314', 'MUSC3240', 'MUSC4270', 'NURS3002', 'NURS7110', 'OHSS4012', 'PHTY4402', 'PHTY4403', 'PHTY4404', 'PHTY7882', 'POLS7125', 'POLS7521', 'PSYC7524', 'PSYC7534', 'PSYC7544', 'PSYC7554', 'PSYC7745', 'PSYC7755', 'PSYC7810', 'PSYC7820', 'PSYC7830', 'PSYC7840', 'PSYC7850', 'PSYC7860', 'PSYC8320', 'PSYC8330', 'PSYC8340', 'SCIE3221']

        for course in courses_with_fucked_weightings:
            self.refresh_course(course)

  
    def get_or_add_course(self, course_code):
        """

        :param course_code: String, 4 letters followed by 4 digits
                                (e.g. MATH1051)
        :return:
        """
        _LOG.info(f"getting course: {course_code}")

        if not is_course_code(course_code):
            return

        sql = """
            SELECT course_code
            FROM course
            WHERE course_code = (%s)
            """

        res = self._db.select(sql, data=(course_code,))

        if res:
            # Could scrape course profile here, but
            # probably safe to assume we've already got it
            return {"course_code": course_code}

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
              %s, %s, %s, %s, %s)
              """

        self._db.commit(
            sql,
            data=(
                course["course_code"],
                title,
                description,
                raw_prereqs,
                course["units"],
                course["semester_offerings"][0],
                course["semester_offerings"][1],
                course["semester_offerings"][2],
                True,
            ),
        )

        self.add_incompatible_courses(course_code, course["incompatible_courses"])

        course_profile_id = course["course_profile_id"]
        if course_profile_id:
            self.refresh_course_profile(course_code, course_profile_id)

        return {"course_code": course_code}

    def refresh_course_profile(self, course_code, course_profile_id):
        _LOG.info(f"refreshing course profile: {course_code}")

        if not is_course_code(course_code):
            return

        sql = "DELETE FROM course_assessment WHERE course_profile_id = '%s'" % (course_profile_id)
        self._db.commit(sql)

        #check if course in course_profile
        sql = "SELECT * FROM course_profile WHERE course_code = '%s'" % (course_code)

        res = self._db.select(sql)

        if not res:
            print('WAS DELETED')
            sql = """
                INSERT INTO course_profile (course_profile_id, course_code)
                VALUES (
                    %s,
                    %s
                )
                """
            self._db.commit(sql)

        course_profile = scrape.course_profile(course_code, course_profile_id)

        if not course_profile:
            return

        self._db.commit(sql, data=(course_profile_id, course_code))

        for assessment in course_profile:
            due_date_raw = assessment.get("due_date", "")
            due_date = format_date(due_date_raw)
            due_date_iso = due_date.isoformat() if due_date else None

            sql = """
                INSERT INTO course_assessment (course_profile_id, assessment_name, due_date, due_date_datetime, weighting, learning_obj, str_weighting)
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s, 
                    %s
                )
                """
            # sql = """
            #     UPDATE course_assessment 
            #     SET str_weighting = %s
            #     WHERE course_profile_id = %s
            #     """
            print('here')
            print(assessment["str_weighting"])
            self._db.commit(
                sql,
                data=(
                    course_profile_id,
                    assessment.get("name").replace("'", "''"),
                    due_date_raw,
                    due_date_iso,
                    assessment["weighting"],
                    assessment["learning_obj"],
                    assessment["str_weighting"]
                ),
            )

        return course_profile

    def add_incompatible_courses(self, course_code, incompatible_courses):
        """

        :param course_code: String, course code of parent
        :param incompatible_courses: List, course code/s as Strings
        :return:
        """
        _LOG.info(
            f"flagging incompatible courses: {course_code} <=/=> {str(incompatible_courses)}"
        )

        last_course_code_prefix = None

        # some incompatible course lists are presented like
        # CSSE1001, 2002, 4004. They really mean, CSSE1001, CSSE2002, etc.
        # So, iterate the (assumed) ordered list and resolve
        for i_course_code in incompatible_courses:
            if is_course_code(i_course_code):
                last_course_code_prefix = i_course_code[:4]
            elif re.fullmatch("[0-9]{4}", i_course_code):
                i_course_code = f"{last_course_code_prefix}{i_course_code}"
                # double check
                if not is_course_code(i_course_code):
                    continue

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

    def refresh_course(self, course_code):
        """

        :param course_code: String, 4 letters followed by 4 digits
                                (e.g. MATH1051)
        :return:
        """
        _LOG.info(f"getting course: {course_code}")

        if not is_course_code(course_code):
            return

        course = scrape.course(course_code)

        if course is None:
            return

        sql = """
            SELECT course_code
            FROM course
            WHERE course_code = (%s)
            """

        res = self._db.select(sql, data=(course_code,))

        if not res:
            # Could scrape course profile here, but
            # probably safe to assume we've already got it
            

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
                %s, %s, %s, %s, %s)
                """

            self._db.commit(
                sql,
                data=(
                    course["course_code"],
                    title,
                    description,
                    raw_prereqs,
                    course["units"],
                    course["semester_offerings"][0],
                    course["semester_offerings"][1],
                    course["semester_offerings"][2],
                    True,
                ),
            )

            self.add_incompatible_courses(course_code, course["incompatible_courses"])

        course_profile_id = course["course_profile_id"]
        if course_profile_id:
            self.refresh_course_profile(course_code, course_profile_id)

        return {"course_code": course_code}

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()







