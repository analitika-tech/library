![Bower](https://img.shields.io/bower/l/library?color=%23000) ![example workflow](https://github.com/analitika-tech/library/actions/workflows/django.yml/badge.svg) [![Python 3.6](https://img.shields.io/badge/python-3.8.1-blue.svg)](https://www.python.org/downloads/release/python-381/) ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/analitika-tech/library?include_prereleases&label=release)

# Library Management Software (LMS)

## Table of Content
* [General](#general)
* [Releases](#releases)
    * [0.0.1 - Alpha](#0.0.1-alpha)
    * [0.0.1 - Beta](#0.0.1-beta)
* [Deployment](#deployment)
## General
Library Management Software (LMS) is a open-source project who provides digital support for library', so they can shift their library management model online. The project is with reason open-source because a lot of school librarys do not have resources to buy or lease this software.

The other reason is that we can improve the software over time and stay up to date with the technology trends.

The web app is built on Django. For fast data migration we use Django REST framework so that the data can be easely migrated to LMS. The app is also fully responsive and will have improvements over time.


## Releases

The releases will first be in beta channel and once they passed have passed the user testing and have been fixed they'll be released into the stable channel.

### 0.0.1 - Alpha

The app is in it's first release cycle and is currently relesed as 0.0.1 Alpha and it's available for testing. As we have deployed the app today we discovered some inconsistencies and bugs which will be fixed in the comming days.

You can find issues that we have discovered and fixes in the release docs table

As we discover issues they will be added to this table. You can track the status of the issues in the issues panel or in this table.

### 0.0.1 - Beta

The beta release is set released for user testing.
As we discover issues they will be added to this table. You can track the status of the issues in the issues panel or in this table.

| ✔️ Expected behaviour        | ❌ Current behaviour | Status |
| -----------                   | -----------           | ----------- |
| Book can be deleted if it's not reseravated or all of them are returned | Can't delete at all | ✔️
| Submit button should adjust to the site (Login or regular submit form) | Constantly the same (Register) | ✔️
| API should save the data | The data is not saving when api request is sent | ✔️
| All user-groups should setup automatically | User need's manualy to add them | ✔️
| On issue delete the issued book's in the reservation should be subtracted by 1 | The returned increese by 1 | ✔️
| All dates should have the same format | The date in issues had other format | ✔️

## Deployment

To deploy the app you first need to find your web host, we used Heroku because it's free and easy to setup but you can use any Cloud provider as you wish (GCP, AWS, Azure).

To run the project localy first clone the project:
``` bash
git clone git@github.com:analitika-tech/library.git
```

Setup the virtual environment:
```bash
# Create the virtual environment
python3 -m venv env

# Activate the virtual environment Linux
source env/bin/activate

# Install the required packages from the requirements.txt
pip install -r requirements.txt
```

After you setup the environment run:
```bash
# To migrate all the DB models
python manage.py migrate

# Setting up all user-groups
python manage.py create_groups

# Run the server by typing
python manage.py runserver
```
