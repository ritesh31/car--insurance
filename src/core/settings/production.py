import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'true').lower() == "true"

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get("DATABASE_URL"))
DEFAULT_CONNECTION.update({"CONN_MAX_AGE": 600})
DATABASES = {"default": DEFAULT_CONNECTION}
ALLOWED_HOSTS = ['*']

FRONTEND_DOMAIN = os.environ.get("FRONTEND_DOMAIN")

# Social
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_TWITTER_KEY = os.environ.get("SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("SOCIAL_AUTH_TWITTER_SECRET")

SOCIAL_AUTH_TWITCH_KEY = os.environ.get("SOCIAL_AUTH_TWITCH_KEY")
SOCIAL_AUTH_TWITCH_SECRET = os.environ.get("SOCIAL_AUTH_TWITCH_SECRET")
SOCIAL_AUTH_TWITCH_SCOPE = os.environ.get("SOCIAL_AUTH_TWITCH_SCOPE")

# Email
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Game
STEAM_API_KEY = os.environ.get("STEAM_API_KEY")
XBOX_AUTHENTICATION_URL = os.environ.get("XBOX_AUTHENTICATION_URL")

TRACKER_NETWORK_API_KEY = os.environ.get("TRACKER_NETWORK_API_KEY")
PUBG_API_KEY = os.environ.get("PUBG_API_KEY")
BRAWALHALLA_API_KEY = os.environ.get("BRAWALHALLA_API_KEY")

# AWS S3
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

# Celery
BROKER_URL = os.environ.get('CLOUDAMQP_URL')

# FCM
FCM_API_KEY = os.environ.get('FCM_API_KEY')
