CRSF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}
	]

GOOGLE_API_CLIENT_ID = 'myid.apps.googleusercontent.com'
GOOGLE_API_CLIENT_SECRET = 'my secret code'
GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'
GOOGLE_OAUTH2_URL = 'https://accounts.google.com/o/oauth2/'
GOOGLE_API_URL = 'https://www.googleapis.com/oauth2/v1/'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')