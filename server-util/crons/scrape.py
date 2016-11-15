from bs4 import BeautifulSoup
import re
import requests
import pprint
import os


class Course:
    """
    Scrapes and holds all data pertaining to course
    """

    @staticmethod
    def get_course(course_code):
        """
        Scrapes title, description, offering and prerequisites for
        given course
        :return: Dict Object, containing course details
        """
        print(course_code + ' GETTING')
        base_url = 'http://www.uq.edu.au/study/course.html?course_code=%s' \
                   % course_code

        r = requests.get(base_url)
        if len(r.content) < 10:
            return None
        soup = BeautifulSoup(r.content, "html.parser")

        course_details = {
            'course_code': course_code,
            'title': soup.find(id="course-title").get_text()[:-11],
            'description': soup.find(id="course-summary").get_text().replace('"', ''),
            'units': int(soup.find(id="course-units").get_text()),
            'semester_offerings': []
        }
        parent_description_elem = soup.find(id="description").contents[1].get_text()
        invalid_match = 'This course is not currently offered, please contact the school.'
        # case for deprecated courses w/ no units (e.g. COMP1500) or other determining factors
        if course_details['units'] < 1 or invalid_match in parent_description_elem:
            print('\t\t\tCOURSE NOT VALID: %s' % course_code)
            return None

        try:
            course_details['raw_prereqs'] = \
                soup.find(id="course-prerequisite").get_text()
        except AttributeError:
            course_details['raw_prereqs'] = ''

        raw_semester_offerings = \
            str(soup.find_all(id="course-current-offerings"))

        if "Semester 1, " in raw_semester_offerings:
            course_details['semester_offerings'].append('1')
        if "Semester 2, " in raw_semester_offerings:
            course_details['semester_offerings'].append('2')
        if "Summer Semester, " in raw_semester_offerings:
            course_details['semester_offerings'].append('3')
        try:
            course_details['course_profile_id'] = soup.find(class_='profile-available')['href'].split('=')[-1]
        except TypeError:
            course_details['course_profile_id'] = '0'

        return course_details

    @staticmethod
    def scrape_cp(course_soup):
        """
        Gets course profile info
        :return:
        """
        return None


class Plan:
    """
    utility class for gathering academic plan details
    """

    @staticmethod
    def scrape_plan(plan_code):
        """
        Scrapes basic data for given program
        :return: None
        """

        base_url = 'https://www.uq.edu.au/study/plan.html?acad_plan=%s' \
                   % plan_code

        r = requests.get(base_url)
        soup = BeautifulSoup(r.content, "html.parser")

        plan_rules = Plan.scrape_plan_rules(plan_code)

        return {
            'program_code': soup.find(id="plan-field-key").get_text(),
            'plan_code': plan_code,
            'course_list': plan_rules['course_list'],
            'rules': plan_rules['rules']
        }

    @staticmethod
    def scrape_plan_rules(plan_code):
        """
        Scrapes rules and courses required for program e.g. Chemistry major
        :return:
        """

        plan_rules = {
            'course_list': [],
            'rules': []
        }

        base_url = 'https://www.uq.edu.au/study/plan_display.html?acad_plan=%s'\
                   % plan_code

        r = requests.get(base_url)
        soup = BeautifulSoup(r.content, "html.parser")
        raw_rules = soup.find_all("div", "courselist")

        # get courses
        raw_courses = soup.find_all("a", href=re.compile("course_code"))

        for course in raw_courses:

            raw_course = course.get_text().strip()
            courseObj = Course.get_course(raw_course)
            if raw_course not in plan_rules['course_list'] and courseObj is not None:
                plan_rules['course_list'].append(raw_course)

        for section in raw_rules:
            rsoup = BeautifulSoup(str(section), "html.parser")
            rule = {
                'text': rsoup.find("p").get_text().strip().replace('\n', '<br>'),
                'courses': []
            }

            raw_courses = rsoup.find_all("a", href=re.compile("course_code"))
            for raw_course in raw_courses:
                rule['courses'].append(raw_course.get_text().strip())

            if len(rule['text']) != 0 and len(rule['courses']) != 0:
                plan_rules['rules'].append(rule)

        return plan_rules


class Program:
    """
    Utility class for gathering program information, eg Bachelor of Science
    """

    @staticmethod
    def scrape_program_details(program_code):
        """

        :param program_code: str, program code for given program (4 digits)
        :return: Dict, program details
        """

        url = "https://www.uq.edu.au/study/program.html?acad_prog=" \
              + str(program_code)

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        program = {
            'program_code': program_code,
            'title': soup.find(id="program-title").get_text(),
            'level': soup.find(id="program-title").get_text().split(' ')[0],
            'abbreviation': soup.find(id="program-abbreviation").get_text(),
            'durationYears': int(soup.find(id="program-domestic-duration").get_text()[0]),
            'units': int(soup.find(id="program-domestic-units").get_text()),
            'major_list': [],
            'course_list': (open('meta/program_course_list/%s.txt' % program_code, 'r')).read().replace(' ', '').split(',')
        }

        raw_majors = soup.find_all('a', href=re.compile("acad_plan"))
        for raw_major in raw_majors:

            # remove extended majors (temporary, consider merging)
            if raw_major.text != 'Extended Major':
                plan_code = raw_major['href'][-10:]
                title = raw_major.text
                program['major_list'].append({
                    'plan_code': plan_code,
                    'title': title
                })

        return program

    @staticmethod
    def scrape_full_program_list(program_code):
        """
        Scrapes list of programs identified by title and program code
        :return: List object, containing dictionaries of program details
        """
        course_list = []
        # selection filter (program_code)

        url = 'https://www.uq.edu.au/study/program_list.html?acad_prog=%s' % program_code

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        raw_courses = soup.find_all("a", href=re.compile("course_code"))
        for raw_course in raw_courses:
            course_list.append(raw_course.get_text().strip())
        print(course_list)
        return course_list


class Catalogue:
    """
    Utility for building catalogue of UQ programs, courses and academic plans
    """

    @staticmethod
    def scrape_program_list():
        """
        Scrapes list of programs identified by title and program code
        :return: List object, containing dictionaries of program details
        """
        program_list = []
        # selection filter (program_code)
        program_selection_filter = ['2342', '2030', '2230']

        url = 'https://www.uq.edu.au/study/browse.html?level=ugpg'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        raw_programs = soup.find_all('a', href=re.compile("acad_prog"))
        for raw_program in raw_programs:
            program_code = raw_program['href'][-4:]
            if program_code in program_selection_filter:
                program = Catalogue.scrape_program(program_code)
                program_list.append(program)
        
        return program_list

    @staticmethod
    def scrape_plan(major):
        """
        Scrapes everything for given plan
        :param major: Dictionary, defining a plan (major)
        :return:
        """

        course_list = []
        raw_course_list = []  # course codes as strings
        flagged_course_list = ['COMP1500']    # invalid courses, etc

        plan = Plan.scrape_plan(major['plan_code'])
        plan['title'] = major['title']
        for course_code in plan['course_list']:
            print("\t\tCOURSE: ", course_code)
            course = Course.get_course(course_code)
            if course_code not in raw_course_list and course is not None:
                print("\t\t\tAVAILABLE: ", course_code)
                course_list.append(course)
                raw_course_list.append(course_code)
        return {
            'course_list': course_list,
            'plan': plan
        }

    @staticmethod
    def scrape_program(program_code):
        """
        Scrapes everything for given plan
        :param major: Dictionary, defining a program (major)
        :return:
        """

        course_list = []
        raw_course_list = []  # course codes as strings
        flagged_course_list = ['COMP1500']    # invalid courses, etc

        program = Program.scrape_program_details(program_code)
        for course_code in program['course_list']:
            course = Course.get_course(course_code)
            if course_code not in raw_course_list and course is not None:
                course_list.append(course)
        return {
            'course_list': course_list,
            'program': program
        }

    

    @staticmethod
    def scrape_catalogue(plan_selection_filter):
        """
        Scrapes everything
        :param plan_selection_filter: List, containing program plan codes NOT to be loaded
        :return: Dict Object, containing all
        """

        print("\n********* SCRAPE INITIALIZED *********\n\n")

        program_list = Catalogue.scrape_program_list()
        plan_list = []
        course_list = []
        raw_course_list = []    # course codes as strings

        plan_selection_filter = {
            'plans': []
        }
        # change line to 'in' from 'not in' for a reverse filter

        dev_count = 0
        for program in program_list:
            print("PROGRAM: ", program['title'])

            for major in program['major_list']:

                if major['plan_code'] not in plan_selection_filter['plans']:
                    print("\n\tMAJOR: ", major['title'])
                    plan = Catalogue.scrape_plan(major)

                    if plan['plan'] not in plan_list:
                        plan_list.append(plan['plan'])

                    for course in plan['course_list']:
                        if course['course_code'] not in raw_course_list:
                            course_list.append(course)
                            raw_course_list.append(course['course_code'])

                    for course in program['course_list']:
                        if course['course_code'] not in raw_course_list:
                            course_list.append(course)
                            raw_course_list.append(course['course_code'])

        print("\n********* SCRAPE COMPLETE *********\n\n")

        catalogue = {
            'program_list': program_list,
            'plan_list': plan_list,
            'course_list': course_list
        }

        Catalogue.export(catalogue)

        return catalogue

    @staticmethod
    def export(data):
        file = open('catalogue.txt', 'w')
        file.write(pprint.pformat(data))
