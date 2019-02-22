import re
import src.scrape.helpers as helpers
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("program_course_list_scraper")

def program_course_list(program_code):
    """
    Scrapes list of courses for given program identified by title and program code
    """
    _LOG.debug(f'scraping program course_list:{program_code}')

    url = f"{settings.UQ_BASE_URL}/programs-courses/program_list.html?acad_prog={program_code}"
    soup = helpers.get_soup(url)

    course_list = []

    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for raw_course in raw_courses:
        course_list.append(raw_course.get_text().strip())

    return course_list
