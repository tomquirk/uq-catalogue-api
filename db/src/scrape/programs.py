"""
Programs scraper
"""
import re
import src.scrape.helpers as helpers
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("programs_scraper")


def programs():
    """
    Scrapes list of programs
    :return: List, of program codes
    """
    _LOG.debug("scraping list of programs")

    programs = []

    url = "https://future-students.uq.edu.au/study/find-a-program/listing/undergraduate"
    soup = helpers.get_soup(url)

    raw_programs = soup.find_all("a", href=re.compile("/study/program"))
    for raw_program in raw_programs:
        program_code = raw_program["href"][-4:]
        programs.append(program_code)

    return programs
