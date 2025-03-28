import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://postgres.lolamzuokwevbtjjfjsr:4a7DinSowBtXP6kg@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key
