"""
Plan scraper
"""
import re
import scrape.helpers as helpers
import settings
from bs4 import BeautifulSoup


def plan(plan_code, plan_title):
    """
    Scrapes basic data for given program
    :return: None
    """
    # base_url = f'{settings.UQ_BASE_URL}/programs-courses/plan.html?acad_plan={plan_code}'

    # soup = helpers.get_soup(base_url)
    soup = BeautifulSoup(open('test/data/plan.html'), 'lxml')

    plan_rules = get_plan_rules(plan_code)

    return {
        'plan_code': plan_code,
        'title': plan_title,
        'program_code': soup.find(id="plan-field-key").get_text(),
        'course_list': plan_rules['course_list'],
        'rules': plan_rules['rules']
    }


def get_plan_rules(plan_code):
    """
    Scrapes rules and courses required for program e.g. Chemistry major
    :return:
    """

    plan_rules = {
        'course_list': [],
        'rules': []
    }

    # base_url = f'{settings.UQ_BASE_URL}/programs-courses/plan_display.html?acad_plan={plan_code}'

    # soup = helpers.get_soup(base_url)
    soup = BeautifulSoup(open('test/data/plan_rules.html'), 'lxml')

    # raw_rules = soup.find_all("div", "courselist")

    # get courses
    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for course in raw_courses:
        if not course:
            continue
        raw_course = course.get_text().strip()
        if raw_course not in plan_rules['course_list']:
            plan_rules['course_list'].append(raw_course)

    # for section in raw_rules:
    #     rsoup = BeautifulSoup(str(section), "lxml")
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
