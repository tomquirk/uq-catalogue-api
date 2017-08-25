"""
Program scraper
"""
import re
import scrape.helpers as helpers


def program(program_code):
    """

    :param program_code: str, program code for given program (4 digits)
    :return: Dict, program details
    """

    url = "https://www.uq.edu.au/study/program.html?acad_prog=" \
        + str(program_code)
    soup = helpers.get_soup(url)

    program_data = {
        'program_code': program_code,
        'title': soup.find(id="program-title").get_text(),
        'level': soup.find(id="program-title").get_text().split(' ')[0].lower(),
        'abbreviation': soup.find(id="program-abbreviation").get_text(),
        'durationYears': int(soup.find(id="program-domestic-duration").get_text()[0]),
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

    url = 'https://www.uq.edu.au/study/program_list.html?acad_prog=%s' % program_code
    soup = helpers.get_soup(url)

    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for raw_course in raw_courses:
        course_list.append(raw_course.get_text().strip())

    return course_list
