# -*- coding=utf-8 -*-
"""
Django settings for jd2 project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from logging import CRITICAL
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#hqz5#kd(s(b(zvmtg+v4^%(ncqbqfo-5-3bc9(epb3+9*-2i_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'app.middleware.CheckSession',
)

ROOT_URLCONF = 'jd2.urls'

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

WSGI_APPLICATION = 'jd2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# # TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'GMT-8'
TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 按手册和网上的方法在settings.py中设置“SESSION_COOKIE_AGE” 和 “SESSION_EXPIRE_AT_BROWSER_CLOSE” 均不生效。
# 通过查看django的源代码"middleware.py"才知道这两个参数只有在
# settings.SESSION_SAVE_EVERY_REQUEST 为True时才有效。
# 依此在settings.py中设置这个变量后问题解决。
# 从源代码看SESSION_EXPIRE_AT_BROWSER_CLOSE为True时 SESSION_COOKIE_AGE 不生效。
# 也就是说用户只能二选一，在浏览器关闭时使session失效 或 超时失效。

# request.session.set_expiry(value) 你可以传递四种不同的值给它： 
# * 如果value是个整数，session会在些秒数后失效（适用于整个Django框架，即这个数值时效时整个页面都会session失效）。 
# * 如果value是个datatime或timedelta，session就会在这个时间后失效。 
# * 如果value是0,用户关闭浏览器session就会失效。 
# * 如果value是None,session会依赖全局session失效策略。


# SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 30  # 单位秒 60*30=30分钟。
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # ：会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效。

# LOGGING_CONFIG = False
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
#         # 日志格式
#     },
#     'filters': {
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/all.log',  # 日志输出文件
#             'maxBytes': 1024 * 1024 * 5,  #文件大小
#             'backupCount': 5,  #备份份数
#             'formatter': 'standard',  #使用哪种formatters日志格式
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/error.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'request_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'scprits_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default', 'console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'django.request': {
#             'handlers': ['request_handler'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'scripts': {
#             'handlers': ['scprits_handler'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         'blog.views': {
#             'handlers': ['default', 'error'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#     }
# }


# TEMPLATE_DIRS = (
# os.path.join(BASE_DIR,  'templates'),
# )
#
# LOGGING = {
# 'version': 1,
# 'disable_existing_loggers': True,
# 'formatters': {
# 'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
#         },
#     },
#     'filters': {
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join('../logs/', 'all.logs'),  # 或者直接写路径：'c:\logs\all.logs',
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'request_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join('../logs/', 'script.logs'),
#             # 或者直接写路径：'filename':'c:\logs\request.logs''
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'scprits_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join('../logs/', 'script.logs'),  # 或者直接写路径：'filename':'c:\logs\script.logs'
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default', 'console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'XieYin.app': {
#             'handlers': ['default', 'console'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#         'django.request': {
#             'handlers': ['request_handler'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'scripts': {  # 脚本专用日志
#                       'handlers': ['scprits_handler'],
#                       'level': 'INFO',
#                       'propagate': False
#                       },
#     }
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     },
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             # 'class': 'logging.StreamHandler',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }