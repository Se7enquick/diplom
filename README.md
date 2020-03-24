# This is my first pet project(https://trello.com clone)
## How to run a project in your localhost
### 1) Clone project using this command: ```git clone git@github.com:Se7enquick/diplom.git```
### 2) Create virtual environment inside the project directory using this command : ```python3 -m virtualenv env```
### 3) You need to install all requirements using command : ```pip install -r requirements.txt```
### 4) In settings.py in ```DATABASES``` field you need to connect your PostgreSQL database and use ```python manage.py migrate``` command. This is little guide how to do it : https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
### 5) Create a superuser using ```python manage.py createsuperuser``` command
### 6) After migrations you can run a localhost using this command ```python manage.py runserver```
### 7) After that login to ```127.0.0.1:8000/admin``` and create 5 status models(whatever you want)
### 8) Now you can use the project
