"""
Plan scraper
"""
import re
import src.scrape.util.helpers as helpers
import src.scrape.util.cache as cache
import src.settings as settings
from src.logger import get_logger

_LOG = get_logger("plan_scraper")


def plan(plan_code):
    """
    Scrapes basic data for given program
    :return: None
    """
    cache_id = f"plan:{plan_code}"
    cached = cache.get(cache_id)
    if cached:
        _LOG.debug(f"using cached plan: {plan_code}")
        return cached

    _LOG.debug(f"scraping plan: {plan_code}")

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

