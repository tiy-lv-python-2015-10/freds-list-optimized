from .settings import *

DATABASES = {
     'default': {
          'ENGINE':'django.db.backends.postgresql_psycopg2',
          'NAME': 'fredslist',
          'USER': 'postgres',
          'PASSWORD': '',
          'HOST': 'localhost',
          'POST':  '',
     }
}