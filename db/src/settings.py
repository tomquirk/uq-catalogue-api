import os

DATABASE = {
    "NAME": os.getenv("DATABASE_NAME", "uq_catalogue"),
    "USER": os.getenv("DATABASE_USER", "postgres"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD", ""),
    "HOST": os.getenv("DATABASE_HOST", "127.0.0.1"),
    "PORT": os.getenv("DATABASE_PORT", "5432"),
}
print(DATABASE["NAME"])
print(DATABASE["USER"])
print(DATABASE["PASSWORD"])
print(DATABASE["HOST"])

UQ_BASE_URL = "https://my.uq.edu.au"
UQ_FUTURE_BASE_URL = "https://future-students.uq.edu.au"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
PROGRAMS_WHITELIST = []
SCRAPE_CACHE_ROOT = 'src/scrape/cache'
# PROGRAMS_WHITELIST = [
#     "2366",
#     "2032",
#     "2033",
#     "2382",
#     "2370",
#     "2386",
#     "2418",
#     "2378",
#     "2387",
#     "2422",
#     "2388",
#     "2419",
# ]  # list of program codes (str)
if not os.path.exists(SCRAPE_CACHE_ROOT):
    os.mkdir(SCRAPE_CACHE_ROOT)
