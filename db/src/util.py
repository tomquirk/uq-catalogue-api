COURSE_REGEX = "[A-Z]{4}[0-9]{4}"  # CSSE1001
PLAN_REGEX = "[0-9]{4}"  # 2424
PRORGAM_REGEX = "[A-Z]{6}[0-9]{4}"  # AGRONX2418

import re


def is_course_code(maybe_course_code):
    return True if re.fullmatch(COURSE_REGEX, maybe_course_code) else False


def is_plan_code(maybe_plan_code):
    return True if re.fullmatch(PLAN_REGEX, maybe_plan_code) else False


def is_program_code(maybe_program_code):
    return True if re.fullmatch(PRORGAM_REGEX, maybe_program_code) else False
