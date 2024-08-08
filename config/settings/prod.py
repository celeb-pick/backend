from .base import *

ALLOWED_HOSTS = ['celebpick.site', '54.180.10.103']

DEBUG = False

REST_FRAMEWORK.update({
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/h',
        'user': '300/h',
    }
})
