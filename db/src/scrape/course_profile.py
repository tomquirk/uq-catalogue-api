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
    if not date or not isinstance(date, str) or not any(char.isdigit() for char in date):
        return None

    dates = date.split("-")
    formatted_date = None
    if len(dates) == 1:
        return dateparser.parse(date)

    date1 = dateparser.parse(dates[0])
    date2 = dateparser.parse(dates[1])
    if date1 and date2 and date1.date() == date2.date():
        return dateparser.parse(dates[0])


def course_profile(course_code, course_profile_id):
    """
    Scrapes a course profile
    :return: Dict Object, containing course profile details
    """
    _LOG.debug(f"scraping course profile: ${course_code}-${course_profile_id}")

    base_url = f"https://course-profiles.uq.edu.au/student_section_loader/section_5/{course_profile_id}"
    try:
        all_tables = pd.read_html(base_url, match="Assessment Task")
        print('profile id: ', course_profile_id)
        print('ALL TABLES\n')
        print(all_tables)

    except ValueError:
        return
    # gets tables containing desired information
    #all_tables = all_tables[2:]
    all_tables = list(all_tables)

    for i, table in enumerate(all_tables):
        if len(table.columns) != 4:
            del all_tables[i]

    assessments = []
    if len(all_tables) > 1:
        for table in all_tables:
            table_assessments = scrape_assessment_table(table, course_code)
            assessments.extend(table_assessments)
        return assessments
    else:
        assessments = []
        for row in all_tables:
            print('ROW')
            print(row)
            if all_tables.index(row) == 0:
                continue
            row = list(row)
            #table_length = table.shape[0] - 1
            i = 1

            name = row[0]
            due_date = row[1]
            str_weighting = row[2]
            try:
                weighting = int(row[2].split("%")[0]) / 100.0
            except Exception:
                weighting = None

            learning_obj = row[3]

            assessment = {
                "course_code": course_code,
                "name": split_name(name),
                "due_date": due_date,
                "weighting": weighting,
                "learning_obj": learning_obj,
                "str_weighting": str_weighting,
            }

            assessments.append(assessment)
        return assessments


def scrape_assessment_table(table, course_code):
    assessments = []
    print('this is the table being passed')
    print(table)
    for row in table:
        if table.index(row) == 0:
            continue
        row = list(row)
        #table_length = table.shape[0] - 1
        i = 1

        name = row[0]
        due_date = row[1]
        str_weighting = row[2]
        try:
            weighting = int(row[2].split("%")[0]) / 100.0
        except Exception:
            weighting = None

        learning_obj = row[3]

        assessment = {
            "course_code": course_code,
            "name": split_name(name),
            "due_date": due_date,
            "weighting": weighting,
            "learning_obj": learning_obj,
            "str_weighting": str_weighting,
        }

        assessments.append(assessment)
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
                return name[index + 1:]
        except IndexError:
            return name
    return name


if __name__ == "__main__":
    x = course_profile("ACCT2112", "95235")
