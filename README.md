
# A Basic Polls App

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.
It consist of two parts: 
1. A public site that lets people view polls and vote in them.
2. An admin site that lets you add, change, and delete polls.


## Requirements

To run this project on your system you will need to have installed:

```bash
    Python 3.10.6
    Django 4.1
    pipenv

```

To install Python and Django please refer to the [Django Quick Installation Guide](https://docs.djangoproject.com/en/4.1/intro/install/)

## Quick Start/ Installation Guide

Clone this repository by using the following command or simply download it.
```bash
  git clone https://github.com/imadroshan/Django-polls-app.git

```

Open it in the editor of your choice and then open the integrated terminal. I am assuming that you have installed Python, Django and pipenv at this point. The next step is to install the dependencies, make migrations, create a database user and running this project by typing in the following commands:
```bash
    cd polling_site

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

    python manage.py runserver
```
Then go to the link in the browers provided to you by your runserver command.
## Documentation

For the detailed documentation please visit: [DjangoProjects](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), Although you will also find comments in the code which explains, what specific function/method is doing. 

