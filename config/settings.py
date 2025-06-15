import os
from pathlib import Path
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# 変更: pythonanywhereのホスト名と、ローカル開発用のホストを追加
ALLOWED_HOSTS = [
    'spaceaoigo.pythonanywhere.com',
    '127.0.0.1',
    'localhost',
]

# 【変更】プロジェクト名を 'Stupre' から 'StudyPress' に変更
PROJECT_NAME = 'StudyPress'

# Application definition

# (一部抜粋)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 3rd party apps
    'bootstrap5',
    'pwa',

    # my apps
    'accounts.apps.AccountsConfig', # ユーザー認証・プロフィール
    'records.apps.RecordsConfig',   # 学習記録・SNS機能
]
# (中略)
# ログイン後のリダイレクト先を学習記録一覧に変更
LOGIN_REDIRECT_URL = 'records:record_list'
LOGOUT_REDIRECT_URL = 'records:record_list'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise: 静的ファイル配信の効率化
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
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
# （確認）言語とタイムゾーンは日本のユーザー向けに設定済みで適切です
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Whitenoise用の設定（本番環境向け）
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# メディアファイル（ユーザーのアイコン画像など）の保存場所
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# （確認）カスタムユーザーモデルの設定は適切です
AUTH_USER_MODEL = 'accounts.CustomUser'

# （確認・提案）ログイン/ログアウト後のリダイレクト先
# 今は投稿一覧ですが、将来的にはダッシュボード（今日のTODO画面など）に変更するのがおすすめです
LOGIN_URL = 'accounts:login'

# django-bootstrap5 の設定
BOOTSTRAP5 = {
    'css_url': {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
    },
    'javascript_bundle_url': {
        'url': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
    },
    # 【提案】ダークモードはCSSで実装しますが、Bootstrapのテーマ機能も利用可能です
    # 例: 'theme_url': 'https://cdn.jsdelivr.net/npm/bootswatch@5/dist/darkly/bootstrap.min.css'
}

# 【追加】PWA（プログレッシブウェブアプリ）のための設定 (要件38)
# ※別途 `pip install django-pwa` が必要です
PWA_APP_NAME = 'StudyPress'
PWA_APP_DESCRIPTION = "大学受験生のための学習管理SNS"
PWA_APP_THEME_COLOR = '#1c1c1e'  # Appleライクなダークモードの背景色をイメージ
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
