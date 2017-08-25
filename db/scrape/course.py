"""
Course scraper
"""
import scrape.helpers as helpers


def course(course_code):
    """
    Scrapes title, description, offering and prerequisites for
    given course
    :return: Dict Object, containing course details
    """
    base_url = 'http://www.uq.edu.au/study/course.html?course_code=%s' \
        % course_code

    soup = helpers.get_soup(base_url)

    if soup is None or soup.find(id="course-notfound"):
        return None

    course_summary = soup.find(
        id="course-summary").get_text().replace('"', '').replace("'", "''")

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

    parent_description_elem = soup.find(
        id="description").contents[1].get_text()
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
        course_details['course_profile_id'] = soup.find(
            class_='profile-available')['href'].split('=')[-1]
    except TypeError:
        course_details['course_profile_id'] = 0

    return course_details


def scrape_cp(course_soup):
    """
    Gets course profile info
    :return:
    """
    return None
