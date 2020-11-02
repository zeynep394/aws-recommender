import os

#from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xb)jhn@1)zgo)rcql1dor!$_nav@dat-95q*$!0e%v=&%n7py('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['IMDb-movie-reccomender-dev.us-east-2.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_recommender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_recommender.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#ÖNEMLİ NOT 
################ Aşağıda belitilen tüm bilgileri düzgün bir şekilde girmezsen bir eksik bile varsa
#conn = _connect(dsn, connection_factory=connection_factory, **kwasync) django.db.utils.OperationalError hatasını veriyor. 
# Bilgileri eksik girmişim düzelttim sql'e ulaşabildi en sonunda ve sorun çıkarmadan bağlandı 
#şimdi amacım postgres databaseinde oluşturduğum movie_data table'ını (IMDb top 250  movie list) modelsdeki fieldlere uygun hale getirerek websitesinde kullanabilmek
#18.09.2020 bir cuma günü saat 18.20 babannem hasta babam karantinada annem işte 6 aydır turgutludan başka bir yere gitmedim. ipad7th gen istiyorum
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',  
        'USER': 'postgres',
        'PASSWORD': 'f1t3S.!klm?',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }

}
#UPDATE movie_data SET pic ='fc.jpg' WHERE id=9;

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL= '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env'),]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

MEDIA_ROOT= os.path.join(VENV_PATH, 'media_root')
