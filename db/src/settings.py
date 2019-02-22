import os

DATABASE = {
    "NAME": os.getenv("DATABASE_NAME", "uq_catalogue"),
    "USER": os.getenv("DATABASE_USER", "postgres"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD", ""),
    "HOST": os.getenv("DATABASE_HOST", "127.0.0.1"),
    "PORT": os.getenv("DATABASE_PORT", "5432"),
}

UQ_BASE_URL = "https://my.uq.edu.au"
ENV = os.getenv("ENV_NAME", "development")
PROGRAMS_WHITELIST = [
    "2366",
    "2032",
    "2033",
    "2382",
    "2370",
    "2386",
    "2418",
    "2378",
    "2387",
    "2422",
    "2388",
    "2419",
]  # list of program codes (str)
