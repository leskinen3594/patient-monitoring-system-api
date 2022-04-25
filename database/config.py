import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PMS_URL')
# print(f"\n [Database] : {SQLALCHEMY_DATABASE_URI} \n")

# SQLALCHEMY_DATABASE_URI = "postgresql://zwidvjcibsmatf:ae0548446b32f5da7d4eb5adedffd7236154b5e31bfa41fe9f97f3b397a807a1@ec2-52-203-118-49.compute-1.amazonaws.com:5432/d8fsmgk016kiq5"