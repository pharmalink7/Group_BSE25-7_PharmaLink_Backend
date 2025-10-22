"""
Production settings for PharmaLink Backend
This file contains production-specific configuration
"""

import os
import dj_database_url
from .settings import *

# Production-specific overrides
DEBUG = False

# Production database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Production allowed hosts
ALLOWED_HOSTS = [
    'pharmalink-backend.onrender.com',
    '127.0.0.1',
    'localhost'
]

# Logging configuration for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/error.log'),
            'formatter': 'verbose',
        },
        'file_access': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/access.log'),
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },

    'loggers': {
        # Django core logs
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        },

        # HTTP request logs
        'django.server': {
            'handlers': ['file_access', 'console'],
            'level': 'INFO',
            'propagate': False,
        },

        # Error logs
        'django.request': {
            'handlers': ['file_error', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },

        # Custom app logs
        'apps': {
            'handlers': ['file_error', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}


# Production CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://pharmalink-frontend.onrender.com",
]

# Production security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Production cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'production-cache',
    }
}

# Production static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Production media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Production admin configuration
ADMIN_URL = 'admin/'

# Production API configuration
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
})

# Production JWT configuration
from datetime import timedelta

SIMPLE_JWT.update({
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
})

# Production database connection settings
DATABASES['default'].update({
    'CONN_MAX_AGE': 600,
    'OPTIONS': {
        'connect_timeout': 10,
        'options': '-c default_transaction_isolation=read_committed'
    }
})

# Production environment validation
def validate_production_environment():
    """Validate that production environment is properly configured"""
    required_env_vars = [
        'SECRET_KEY',
        'DATABASE_URL',
    ]
    
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Validate database URL format
    db_url = os.environ.get('DATABASE_URL')
    if db_url and not db_url.startswith('postgresql://'):
        raise ValueError("DATABASE_URL must be a PostgreSQL connection string for production")

# Run validation on startup
validate_production_environment()
