"""
Plan scraper
"""
import re
import src.scrape.helpers as helpers
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("plan_scraper")


def plan(plan_code):
    """
    Scrapes basic data for given program
    :return: None
    """
    _LOG.info(f"Scraping plan: {plan_code}")
    base_url = (
        f"{settings.UQ_BASE_URL}/programs-courses/plan.html?acad_plan={plan_code}"
    )
    soup = helpers.get_soup(base_url)

    if not soup:
        return

    program_code = soup.find(id="plan-field-key")

    if program_code:
        program_code = program_code.get_text()

    return {"plan_code": plan_code, "program_code": program_code}

