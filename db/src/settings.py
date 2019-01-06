import os

DATABASE = {
    'NAME': os.getenv('DATABASE_NAME', 'uq_catalogue'),
    'USER': os.getenv('DATABASE_USER', 'root'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
    'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
    'PORT': os.getenv('DATABASE_PORT', '5432'),
}

UQ_BASE_URL = 'https://my.uq.edu.au'
ENV = os.getenv('ENV_NAME', 'dev')
PROGRAMS_WHITELIST = ['2030', '2342']   # list of program codes (str)

INVALID_COURSES_FILEPATH = 'invalid_courses.txt'
INCOMPATIBLE_COURSES_FILEPATH = 'incompatible_courses.txt'
