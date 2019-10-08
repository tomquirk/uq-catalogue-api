import pandas as pd
import re
import dateparser

import src.scrape.util.helpers as helpers
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("course_profile_scraper")


def format_date(date):
    _LOG.debug(f"format_date: {date}")
    # check if date contains no digits
    if not date or isinstance(date, str) and not any(char.isdigit() for char in date):
        return None

    dates = date.split("-")
    if len(dates) > 1:
        date1 = dateparser.parse(dates[0])
        date2 = dateparser.parse(dates[1])
        if date1 and date2:
            if date1.date() == date2.date():
                date = dates[0]
                return dateparser.parse(date)
    date = dateparser.parse(date)
    return date


def course_profile(course_code, course_profile_id):
    """
    Scrapes a course profile
    :return: Dict Object, containing course profile details
    """
    _LOG.debug(f"scraping course profile: {course_code} (cp={course_profile_id})")

    base_url = f"https://www.courses.uq.edu.au/student_section_loader.php?section=5&profileId={course_profile_id}"
    try:
        all_tables = pd.read_html(base_url, match="Assessment Task")

    except ValueError:
        return
    # gets tables containing desired information
    all_tables = all_tables[2:]
    for i, table in enumerate(all_tables):
        if len(table.columns) != 4:
            del all_tables[i]

    assessments = []
    for table in all_tables:
        table_length = table.shape[0] - 1
        i = 1

        while i <= table_length:

            name = table.at[i, 0]
            due_date = table.at[i, 1]
            try:
                weighting = int(table.at[i, 2].split("%")[0]) / 100.0
            except Exception:
                weighting = None
            learning_obj = table.at[i, 3]

            assessment = {
                "course_code": course_code,
                "name": split_name(name),
                "due_date": format_date(due_date),
                "weighting": weighting,
                "learning_obj": learning_obj,
            }
            assessments.append(assessment)

            i += 1

    return assessments


def split_name(name):  # Separates assessment type from assessment name
    for index, letter in enumerate(name):
        try:
            if (
                letter.islower()
                and name[index + 1].isupper()
                or letter == ")"
                and name[index + 1].isupper()
            ):
                return name[index + 1 :]
        except IndexError:
            return name
    return name


if __name__ == "__main__":
    x = course_profile("ACCT2112", "95235")
