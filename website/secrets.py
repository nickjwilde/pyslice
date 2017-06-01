
#/usr/bin/python

#use this file to declare important information. copy this file and save it as secrets.py.

# used to specify the database you would use
engines = {
    'mysql': 'django.db.backends.mysql',
    'sqlite': 'django.db.backends.sqlite3',
    'oracle': 'django.db.backends.oracle',
    'postgres': 'django.db.backends.postgresql'
}

DB_ENGINE = engines['sqlite']
DB_HOST = ''
DB_PORT = ''
DB_NAME = 'pyslice.db'
DB_USERNAME = ''
DB_PASSWORD = ''

SECRET_KEY = '011c5a21314bee98a6d5c33102aab4e1b788979d2068e6a141bf8e71cd1c50f9'
