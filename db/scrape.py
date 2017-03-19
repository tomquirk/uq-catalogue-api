"""
Scrape
"""

import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Course(object):
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
        base_url = 'http://www.uq.edu.au/study/course.html?course_code=%s' \
                   % course_code

        r = requests.get(base_url)
        if len(r.content) < 10:
            return None
        soup = BeautifulSoup(r.content, "html.parser")

        if soup.find(id="course-notfound"):
            return None

        course_summary = soup.find(id="course-summary").get_text().replace('"', '').replace("'", "''")

        # handle edge-case (see STAT2203)
        if '\n' in course_summary:
            course_summary = course_summary.split('\n')[0]

        course_details = {
            'course_code': course_code,
            'title': soup.find(id="course-title").get_text()[:-11].replace("'", "''"),
            'description': course_summary,
            'units': int(soup.find(id="course-units").get_text()),
            'semester_offerings': ['false', 'false', 'false']
        }

        parent_description_elem = soup.find(id="description").contents[1].get_text()
        invalid_match = 'This course is not currently offered, please contact the school.'
        # case for deprecated courses w/ no units (e.g. COMP1500) or other determining factors
        if course_details['units'] < 1 or invalid_match in parent_description_elem:
            print('\t\tCOURSE NOT VALID: %s' % course_code)
            return None

        try:
            course_details['raw_prereqs'] = \
                soup.find(id="course-prerequisite").get_text()
        except AttributeError:
            course_details['raw_prereqs'] = None

        try:
            course_details['incompatible_courses'] = \
                soup.find(id="course-incompatible").get_text()\
                    .replace(' and ', ', ') \
                    .replace(' or ', ', ') \
                    .replace(' & ', ', ') \
                    .replace('; ', ', ') \
                    .split(', ')

        except AttributeError:
            course_details['incompatible_courses'] = None

        raw_semester_offerings = \
            str(soup.find_all(id="course-current-offerings"))

        if "Semester 1, " in raw_semester_offerings:
            course_details['semester_offerings'][0] = 'true'
        if "Semester 2, " in raw_semester_offerings:
            course_details['semester_offerings'][1] = 'true'
        if "Summer Semester, " in raw_semester_offerings:
            course_details['semester_offerings'][2] = 'true'
        try:
            course_details['course_profile_id'] = soup.find(class_='profile-available')['href'].split('=')[-1]
        except TypeError:
            course_details['course_profile_id'] = 0

        return course_details

    @staticmethod
    def scrape_cp(course_soup):
        """
        Gets course profile info
        :return:
        """
        return None


class Plan(object):
    """
    utility class for gathering academic plan details
    """

    @staticmethod
    def get_plan(plan_code, plan_title):
        """
        Scrapes basic data for given program
        :return: None
        """
        base_url = 'https://www.uq.edu.au/study/plan.html?acad_plan=%s' % plan_code

        r = requests.get(base_url)
        soup = BeautifulSoup(r.content, "html.parser")

        plan_rules = Plan.get_plan_rules(plan_code)

        return {
            'plan_code': plan_code,
            'title': plan_title,
            'program_code': soup.find(id="plan-field-key").get_text(),
            'course_list': plan_rules['course_list'],
            'rules': plan_rules['rules']
        }

    @staticmethod
    def get_plan_rules(plan_code):
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
            if raw_course not in plan_rules['course_list']:
                plan_rules['course_list'].append(raw_course)

        # for section in raw_rules:
        #     rsoup = BeautifulSoup(str(section), "html.parser")
        #     rule = {
        #         'text': rsoup.find("p").get_text().strip().replace('\n', '<br>'),
        #         'courses': []
        #     }

        #     raw_courses = rsoup.find_all("a", href=re.compile("course_code"))
        #     for raw_course in raw_courses:
        #         rule['courses'].append(raw_course.get_text().strip())

        #     if len(rule['text']) != 0 and len(rule['courses']) != 0:
        #         plan_rules['rules'].append(rule)

        return plan_rules


class Program(object):
    """
    Utility class for gathering program information, eg Bachelor of Science
    """

    @staticmethod
    def get_program(program_code):
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
            'level': soup.find(id="program-title").get_text().split(' ')[0].lower(),
            'abbreviation': soup.find(id="program-abbreviation").get_text(),
            'durationYears': int(soup.find(id="program-domestic-duration").get_text()[0]),
            'units': int(soup.find(id="program-domestic-units").get_text()),
            'plan_list': [],
            'course_list': Program.get_program_course_list(program_code)
        }

        raw_plans = soup.find_all('a', href=re.compile("acad_plan"))

        for raw_plan in raw_plans:
            # remove extended majors (temporary, consider merging)
            if raw_plan.text != 'Extended Major':
                plan_code = raw_plan['href'][-10:]
                title = raw_plan.text
                program['plan_list'].append({
                    'plan_code': plan_code,
                    'title': title
                })
        return program

    @staticmethod
    def get_program_course_list(program_code):
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

        return course_list


class Catalogue(object):
    """
    Utility for gathering top-level data from the UQ Catalogue
    """

    @staticmethod
    def get_program_list():
        """
        Scrapes list of programs identified by title and program code
        :return: List object, containing dictionaries of program details
        """
        program_list = []
        # selection filter (program_code)
        program_selection_filter = ['2030', '2342']

        url = 'https://www.uq.edu.au/study/browse.html?level=ugpg'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        raw_programs = soup.find_all('a', href=re.compile("acad_prog"))
        for raw_program in raw_programs:
            program_code = raw_program['href'][-4:]
            if program_code in program_selection_filter:
                program_list.append(program_code)

        return program_list

if __name__ == "__main__":
    Course.get_course('ENGG1100')
