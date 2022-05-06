
# Introduction

The goal of this project is to upload multiple image files, save the image and return the image url back as response in one request
Template is written with django 4.0.4 and python 3 in mind.

      

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/budescode/django-multiple-file-upload.git
    $ cd multiplefilesupload
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py makemigrations
    
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
