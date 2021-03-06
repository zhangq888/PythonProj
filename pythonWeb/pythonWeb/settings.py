"""
Django settings for pythonWeb project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'arj$&wpvv*1*31t6vtgcj))=wrnwv7ev4qai)ph6%9q=ww22rl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # app项目配置
    'blog.apps.FirstwebConfig',
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

ROOT_URLCONF = 'pythonWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates')],
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

WSGI_APPLICATION = 'pythonWeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# 检查有没有将app加到settings里面的INSTALLED_APPS里，
# 执行python manager.py makemigrations 生成migrations文件
# 然后再执行python manager.py migrate  生成数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usm',
        'USER': 'root',
        'PASSWORD': '111111',
        'HOST': '',
        'PORT': '',
    }
}

# http://blog.csdn.net/foryouslgme/article/details/52154152
# MySQLdb只支持Python2.，还不支持3.
# 可以用PyMySQL代替。
#
# 安装方法：
# pip install PyMySQL
# 然后在需要的项目中，把 init.py中添加两行：
#
# import pymysql
# pymysql.install_as_MySQLdb()
#
# 就可以用 import MySQLdb了。其他的方法与MySQLdb一样。
#
# django连接mysql时的错误处理
# 找到mysql连接文件：D:\Program Files (x86)\Python35\Lib\site-packages\django\db\backends\mysql\__init__.py
# 添加
# import pymysql
# pymysql.install_as_MySQLdb()


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE：用于存放本地时区信息，默认值为UTC，意思为采用国际标准时间“格林尼治时间”。
# 中国处于东八区，官方文档上有两个取值“Asia/Shanghai”和“Asia/Chongqing”(没有北京).
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ：用于控制是否使用UTC时间(True and False)。如果设置为False，则使用本地时间。
# 为了保证世界各地时间统一性，可以在数据库中使用UTC时间，根据需求转换成相应时区时间。
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
