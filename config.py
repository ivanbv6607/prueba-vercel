import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'DATABASE_URL=postgres://neondb_owner:npg_3TNDe1dSzKlO@ep-broad-butterfly-a4d52wfr-pooler.us-east-1.aws.neon.tech/verceldb sslmode=require')
                                        #'postgres://postgres.lolamzuokwevbtjjfjsr:4a7DinSowBtXP6kg@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key
