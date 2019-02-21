"""
Program scraper
"""
import re
import src.scrape.helpers as helpers
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("program_scraper")


def program(program_code):
    """

    :param program_code: str, program code for given program (4 digits)
    :return: Dict, program details
    """
    _LOG.info(f"Scraping program: {program_code}")
    url = (
        f"{settings.UQ_BASE_URL}/programs-courses/program.html?acad_prog={program_code}"
    )
    soup = helpers.get_soup(url)

    program_title = soup.find(id="program-title")
    if program_title:
        program_title = program_title.get_text()

    abbreviation = soup.find(id="program-abbreviation")
    if abbreviation:
        abbreviation = abbreviation.get_text()

    durationYears = soup.find(id="program-domestic-duration")
    if durationYears:
        durationYears = float(durationYears.get_text().strip().split(" ")[0])

    units = soup.find(id="program-domestic-units")
    if units:
        units = int(units.get_text())

    program_data = {
        "program_code": program_code,
        "title": program_title,
        "level": program_title.split(" ")[0].lower(),
        "abbreviation": abbreviation,
        "durationYears": durationYears,
        "units": units,
        "plans": [],
    }

    raw_plans = soup.find_all("a", href=re.compile("acad_plan"))

    for raw_plan in raw_plans:
        # remove extended majors (temporary, consider merging)
        if raw_plan.text != "Extended Major":
            plan_code = raw_plan["href"][-10:]
            title = raw_plan.text
            program_data["plans"].append({"plan_code": plan_code, "title": title})

    return program_data
