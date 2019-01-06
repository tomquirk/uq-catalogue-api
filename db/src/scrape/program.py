"""
Program scraper
"""
import re
import scrape.helpers as helpers
import settings


def program(program_code):
    """

    :param program_code: str, program code for given program (4 digits)
    :return: Dict, program details
    """
    url = f"{settings.UQ_BASE_URL}/programs-courses/program.html?acad_prog={program_code}"
    soup = helpers.get_soup(url)

    program_title = soup.find(id="program-title").get_text()

    program_data = {
        'program_code': program_code,
        'title': program_title,
        'level': program_title.split(' ')[0].lower(),
        'abbreviation': soup.find(id="program-abbreviation").get_text(),
        'durationYears': int(soup.find(id="program-domestic-duration").get_text().strip().split(' ')[0]),
        'units': int(soup.find(id="program-domestic-units").get_text()),
        'plan_list': [],
        'course_list': get_program_course_list(program_code)
    }

    raw_plans = soup.find_all('a', href=re.compile("acad_plan"))

    for raw_plan in raw_plans:
        # remove extended majors (temporary, consider merging)
        if raw_plan.text != 'Extended Major':
            plan_code = raw_plan['href'][-10:]
            title = raw_plan.text
            program_data['plan_list'].append({
                'plan_code': plan_code,
                'title': title
            })

    return program_data


def get_program_course_list(program_code):
    """
    Scrapes list of programs identified by title and program code
    :return: List object, containing dictionaries of program details
    """
    course_list = []
    # selection filter (program_code)

    url = f'{settings.UQ_BASE_URL}/programs-courses/program_list.html?acad_prog={program_code}'
    soup = helpers.get_soup(url)

    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for raw_course in raw_courses:
        course_list.append(raw_course.get_text().strip())

    return course_list
