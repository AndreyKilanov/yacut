import os
from string import ascii_letters, digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')


# for generate short url
APPROVED_SYMBOLS = ascii_letters + digits
LENGTH_SHORT_ID = 6

# for api symbols short
API_SYMBOLS_SHORT = f'^[{APPROVED_SYMBOLS}]+$'

# maximum link length
MAX_LENGTH_ORIGINAL = 512
MAX_LENGTH_CUSTOM = 16
