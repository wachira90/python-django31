# python-django31
python-django31

django-admin version

3.1.7

````
pip install Django==3.1.7


django-admin startproject myapp

python manage.py help

myapp/settings.py

DEBUG = True

python manage.py runserver
````


## setting file myapp/settings.py
````
INSTALLED_APPS = [

    'django.contrib.admin',
    
    'django.contrib.auth',
    
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    
    'django.contrib.messages',
    
    'django.contrib.staticfiles',
    
    'myapp',
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
````

## migrate command
````
python manage.py migrate

python manage.py createsuperuser

C:\Users\admin\myapp>python manage.py createsuperuser

Username (leave blank to use 'admin'):

Email address: wachira@example.com

Password:

Password (again):

The password is too similar to the username.

This password is too short. It must contain at least 8 characters.

Bypass password validation and create user anyway? [y/N]: y

Superuser created successfully.

C:\Users\admin\myapp>


python manage.py runserver

python manage.py runserver 0:8080
````
