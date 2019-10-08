"""
Course scraper
"""
import src.scrape.util.helpers as helpers
import src.settings as settings
from src.logger import get_logger
from src.scrape.util.cache import get_html, set_html
import re

_LOG = get_logger("course_scraper")


def course(course_code):
    """
    Scrapes title, description, offering and prerequisites for
    given course
    :return: Dict Object, containing course details, False if not offerred, None if not a course
    """
    _LOG.debug(f"scraping course: {course_code}")

    cache_id = f'course:{course_code}'
    soup = get_html(cache_id)
    if not soup:
        base_url = (
            f"{settings.UQ_BASE_URL}/programs-courses/course.html?course_code={course_code}"
        )
        soup = helpers.get_soup(base_url)
        set_html(cache_id, str(soup))

    if soup is None or soup.find(id="course-notfound"):
        return

    course_summary_raw = soup.find(id="course-summary")

    course_summary = None
    if course_summary_raw:
        course_summary = (
            course_summary_raw.get_text().replace('"', "").replace("'", "''")
        )

        # handle edge-case (see STAT2203)
        if "\n" in course_summary:
            course_summary = course_summary.split("\n")[0]

    try:
        parent_description_elem = soup.find(
            id="description").contents[1].get_text()
        not_offered_match = (
            "This course is not currently offered, please contact the school."
        )
        # return false if course not offerred
        if not_offered_match in parent_description_elem:
            return False
    except Exception:
        pass

    try:
        raw_units = soup.find(id="course-units").get_text()
        units = int(raw_units)
    except (TypeError, AttributeError):
        return False

    if units < 1:
        return False

    title = soup.find(id="course-title")
    if title:
        title = title.get_text()[:-11].replace("'", "''")

    course = {
        "course_code": course_code,
        "title": title,
        "description": course_summary,
        "units": int(units),
        "semester_offerings": ["false", "false", "false"],
    }

    try:
        course["raw_prereqs"] = soup.find(id="course-prerequisite").get_text()
    except AttributeError:
        course["raw_prereqs"] = None

    try:
        course["incompatible_courses"] = (
            soup.find(id="course-incompatible")
            .get_text()
            .replace(" and ", ", ")
            .replace(" or ", ", ")
            .replace(" & ", ", ")
            .replace("; ", ", ")
            .replace(" + ", ", ")
            .replace("/", ", ")
            .replace("(", "")
            .replace(")", "")
            .split(", ")
        )

    except AttributeError:
        course["incompatible_courses"] = []

    raw_semester_offerings = str(soup.find_all(id="course-current-offerings"))

    if "Semester 1, " in raw_semester_offerings:
        course["semester_offerings"][0] = "true"
    if "Semester 2, " in raw_semester_offerings:
        course["semester_offerings"][1] = "true"
    if "Summer Semester, " in raw_semester_offerings:
        course["semester_offerings"][2] = "true"
    try:
        # import ipdb; ipdb.set_trace()
        course_profile_id_elm = soup.find_all(id="course-offering-2-profile")
        print(course_profile_id_elm)
        if course_profile_id_elm:
            course_profile_id_href = str(
                course_profile_id_elm[0].find("a", recursive=False)['href'])
            #profileID = course_profile_id_href.split('/')[-1]
            profileID = course_profile_id_href[-5:]

        else:
            profileID = None

        # print(course_profile_id_href)
        # print(profileID)
        course["course_profile_id"] = profileID
        # print(course["course_profile_id"])
    except TypeError:
        course["course_profile_id"] = 0

    return course
