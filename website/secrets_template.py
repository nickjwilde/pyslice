#/usr/bin/python

#use this file to declare important information. copy this file and save it as secrets.py.

# used to specify the database you would use
engines = {
    'mysql': 'django.db.backends.mysql',
    'sqlite': 'django.db.backends.sqlite3',
    'oracle': 'django.db.backends.oracle',
    'postgres': 'django.db.backends.postgresql',
    'default': 'django.db.backedns.sqlite3'
}


DB_ENGINE = engines['default']
DB_HOST = ''
DB_PORT = ''
DB_NAME = ''
DB_USERNAME = ''
DB_PASSWORD = ''

SECRET_KEY = ''
