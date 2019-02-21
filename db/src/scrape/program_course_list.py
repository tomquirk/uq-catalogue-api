import re
import src.scrape.helpers as helpers
import src.settings as settings


def program_course_list(program_code):
    """
    Scrapes list of programs identified by title and program code
    :return: List object, containing dictionaries of program details
    """
    course_list = []
    # selection filter (program_code)

    url = f"{settings.UQ_BASE_URL}/programs-courses/program_list.html?acad_prog={program_code}"
    soup = helpers.get_soup(url)

    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for raw_course in raw_courses:
        course_list.append(raw_course.get_text().strip())

    return course_list
