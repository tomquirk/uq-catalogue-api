import re
import src.scrape.util.helpers as helpers
import src.scrape.util.cache as cache
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("plan_rules_scraper")


def plan_rules(plan_code):
    """
    Scrapes rules and courses required for program e.g. Chemistry major
    :return:
    """
    cache_id = f"plan_rules:{plan_code}"
    cached = cache.get(cache_id)
    if cached:
        _LOG.debug(f"using cached plan rules: {plan_code}")
        return cached

    _LOG.debug(f"scraping plan rules: {plan_code}")

    base_url = f"{settings.UQ_BASE_URL}/programs-courses/plan_display.html?acad_plan={plan_code}"
    soup = helpers.get_soup(base_url)

    # raw_rules = soup.find_all("div", "courselist")

    # get courses
    plan_rules = {"course_list": [], "rules": []}
    raw_courses = soup.find_all("a", href=re.compile("course_code"))
    for course in raw_courses:
        if not course:
            continue
        raw_course = course.get_text().strip()
        if raw_course not in plan_rules["course_list"]:
            plan_rules["course_list"].append(raw_course)

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
    cache.set(cache_id, plan_rules)
    return plan_rules
