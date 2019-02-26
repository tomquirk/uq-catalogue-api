import re
import src.scrape.util.helpers as helpers
import src.scrape.util.cache as cache
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("program_course_list_scraper")


def program_course_list(program_code):
    """
    Scrapes list of courses for given program identified by title and program code
    """
    cache_id = f"program_course_list:{program_code}"
    cached = cache.get(cache_id)
    if cached:
        _LOG.debug(f"using cached program course list:{program_code}")
        return cached

    _LOG.debug(f"scraping program course list:{program_code}")
    url = f"{settings.UQ_BASE_URL}/programs-courses/program_list.html?acad_prog={program_code}"
    soup = helpers.get_soup(url)

    course_list = []

    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for raw_course in raw_courses:
        course_list.append(raw_course.get_text().strip())

    cache.set(cache_id, course_list)
    return course_list
