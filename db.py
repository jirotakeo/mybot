from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'netology',
#         'USER': 'postgres',
#         'PASSWORD': 'mysecretpassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@127.0.0.1:5432/netology")

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
