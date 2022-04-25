import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PMS_URL')
# print(f"\n [Database] : {SQLALCHEMY_DATABASE_URI} \n")
