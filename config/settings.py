import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'spaceaoigo.pythonanywhere.com',
    '127.0.0.1',
    'localhost',
]

# プロジェクト名を 'StudyPress' に設定
PROJECT_NAME = 'StudyPress'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 3rd party apps
    'django_bootstrap5', # 正しいライブラリ名に修正
    'pwa',
    'tailwind',
    'theme',             # `tailwind init`で作成されるアプリ

    # my apps
    'accounts.apps.AccountsConfig',
    'records.apps.RecordsConfig',
    # 'planner.apps.PlannerConfig',      # 今後のための準備
    # 'analytics.apps.AnalyticsConfig',  # 今後のための準備
    # 'timer.apps.TimerConfig',          # 今後のための準備
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # プロジェクト名を全てのテンプレートで使えるようにする
                'config.context_processors.project_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Login / Logout Redirect URLs
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'records:record_list'
LOGOUT_REDIRECT_URL = 'records:record_list'

# django-bootstrap5 Settings
BOOTSTRAP5 = {
    'css_url': {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
    },
    'javascript_bundle_url': {
        'url': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
    },
}

# PWA (Progressive Web App) Settings
PWA_APP_NAME = 'StudyPress'
PWA_APP_DESCRIPTION = "大学受験生のための学習管理SNS"
PWA_APP_THEME_COLOR = '#1c1c1e'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/icon-192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'sizes': '512x512'
    }
]
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

# Tailwind CSS Settings
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]
