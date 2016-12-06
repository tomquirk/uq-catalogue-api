from scrape import *
import pymysql


class PostDB:
    """
    Builds database (full wipe, no diff)
    """
    def __init__(self):
        #   MySQL config
        mysqlUser = input('MYSQL username: ')
        mysqlPass = input('MYSQL password: ')
        self._db = pymysql.connect("localhost", mysqlUser, mysqlPass, "uq_catalogue")
        self._cursor = self._db.cursor()

        self._prerequisite_set_count = 0

        self._blacklist = ['COMP1500']  # temporary, should be moved to scrape.py

    def reset(self):
        """
        Clears DB, truncating each table in order of dependency
        :return: None
        """
        queries = [
                   'DELETE from Plan_Course_List',
                   'DELETE from Course_Semester_Offering',
                   'DELETE from Course', 'DELETE from Plan',
                   'DELETE from Program'
        ]

        for sql in queries:
            self.dbexec(sql)

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

        sql = 'SELECT * FROM `Plan`'

        self._cursor.execute(sql)

        data = self._cursor.fetchall()

        for row in data:
            state['plans'].append(row[0])

        sql = 'SELECT * FROM `Program`'

        self._cursor.execute(sql)

        data = self._cursor.fetchall()

        for row in data:
            state['programs'].append(row[0])

        sql = 'SELECT * FROM `Course`'

        self._cursor.execute(sql)

        data = self._cursor.fetchall()

        for row in data:
            state['courses'].append(row[0])

        return state

    def init_catalogue(self):
        """
        Builds and returns course
        :return: None
        """
        state = self.get_state()
        file = open('catalogue.txt', 'r')
        catalogue = file.read()
        if len(catalogue) == 0:
            catalogue = Catalogue.scrape_catalogue(state)
        else:
            catalogue = eval(catalogue)

        pprint.pprint(catalogue)

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
        sql = 'INSERT INTO `Program` ' \
              '(`program_code`, `title`, `level`, `abbreviation`, `durationYears`, `units`) '\
              'VALUES ("%s", "%s", "%s", "%s", "%d", "%d")' % \
              (program['program_code'], program['title'],
               program['level'], program['abbreviation'],
               program['durationYears'], program['units'])

        self.dbexec(sql)

    def add_plan(self, plan):
        """

        :param plan: Dictionary
        :return:
        """
        sql = 'INSERT INTO `Plan` ' \
              '(`plan_code`, `program_code`, `title`) ' \
              'VALUES ("%s", "%s", "%s")' % \
              (plan['plan_code'], plan['program_code'],
               plan['title'])

        self.dbexec(sql)

        for course_code in plan['course_list']:
            if course_code in plan['required_course_list']:
                isRequired = 1
            isRequired = 0
            self.add_plan_course_list(plan['plan_code'], course_code, isRequired)

    def add_course(self, course):
        """

        :param course: Dictionary
        :return:
        """
        print("\nADDING: " + course['course_code'] + " to `Course`")
        sql = 'INSERT INTO `Course` ' \
              '(`course_code`, `title`, `description`, `raw_prerequisites`,' \
              ' `units`, `course_profile_id`) VALUES ("%s", "%s", "%s", "%s", "%d", "%s")' % \
              (course['course_code'], course['title'],
               course['description'], course['raw_prereqs'],
               course['units'], course['course_profile_id'])

        self.dbexec(sql)
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

        sql = 'INSERT INTO `Course_Semester_Offering` (`course_code`, `semester_offering`) ' \
              'VALUES ("%s", "%s")' % \
              (course_code, semester_offering)

        self.dbexec(sql)

    def add_plan_course_list(self, plan_code, course_code):
        """

        :param plan_code:
        :param course_code:
        :return:
        """
        sql = 'INSERT INTO `Plan_Course_list` (`course_code`, `plan_code`, `required`) ' \
              'VALUES ("%s", "%s", "%d")' % \
              (course_code, plan_code, required)

        self.dbexec(sql)

    def dbexec(self, sql_query):
        """
        Helper method for executing queries on db via PyMySQL
        :param sql_query: String, query to be executed
        :return:
        """
        try:
            self._cursor.execute(sql_query)
            self._db.commit()
        except Exception as e:
            print('ERROR at query:', sql_query)
            raise e

x = PostDB()
x.reset()
x.init_catalogue()
