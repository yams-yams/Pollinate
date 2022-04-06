import os

class Config(obj):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'haha_you_dont_know'
    