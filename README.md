# GUDLFT-registration 

## Table of contents

1. [General info](#1-general-info)
    - [original request](#a-original-request)
    - [current repository](#b-current-repository)
2. [Technologies](#2-technologies)
3. [Setup for unix](#3-setup-for-unix)
4. [Tests](#4-tests)
5. [Branches details](#5-branches-details)
6. [Author](#6-author)


## 1. General info
### A) *Original request*

The legacy is a proof of concept (POC) project to show a light-weight version of competition booking platform (*GUDLFT*). The aim is the keep things as light as possible, and use feedback from the users to iterate. It needs to be tested, refactored, optimised and some new functionnalities are expected.
Also, the first version crash and it needs to be fixed. [OriginalRepository](https://github.com/OpenClassrooms-Student-Center/Python_Testing).

### B) *Current repository*

This repository contain 12 branches merged to main. Answers to [issues](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues), test the application (Unit test, integrations test, "functionnals" test and performance test) and add a "Display bord".
After using this application, some more issues had to be patched.
[Go to Branches Details](https://github.com/ValentinPhB/QA-Tests-Debugs-GUDLFT-P11/edit/main/README.md#5-branches-details).


## 2. Technologies

Python 3.10.0

* attrs==21.4.0
* autopep8==1.6.0
* backports.entry-points-selectable==1.1.0
* Brotli==1.0.9
* certifi==2021.10.8
* charset-normalizer==2.0.10
* click==7.1.2
* ConfigArgParse==1.5.3
* coverage==6.2
* distlib==0.3.3
* filelock==3.3.2
* Flask==2.0.2
* Flask-BasicAuth==0.2.0
* Flask-Cors==3.0.10
* gevent==21.12.0
* geventhttpclient==1.5.3
* greenlet==1.1.2
* idna==3.3
* iniconfig==1.1.1
* itsdangerous==2.0.1
* Jinja2==3.0.3
* locust==2.5.1
* MarkupSafe==2.0.1
* msgpack==1.0.3
* packaging==21.3
* platformdirs==2.4.0
* pluggy==1.0.0
* psutil==5.9.0
* py==1.11.0
* pycodestyle==2.8.0
* pyparsing==3.0.6
* pytest==6.2.5
* pytest-flask==1.2.0
* pytest-mock==3.6.1
* pyzmq==22.3.0
* requests==2.27.1
* roundrobin==0.0.2
* six==1.16.0
* toml==0.10.2
* typing-extensions==4.0.1
* urllib3==1.26.8
* virtualenv==20.9.0
* Werkzeug==2.0.2
* zope.event==4.5.0
* zope.interface==5.4.0

## 3. Setup for Unix

__Original data is unusable. Competition's dates are passed so you can't book places.
tests/unit_test/conftest.py client(s) fixtures mock data to fix this.__
__That's why this README.md dont show you how to test this application from browser.__

Only first-time use :
After downloading QA-Tests-Debugs-GUDLFT-P11.main from Github, extract it to a location of your choice (exemple : "PATH").
Or if you use git, download it from [here](https://github.com/ValentinPhB/QA-Tests-Debugs-GUDLFT-P11).

Create a virtual environment in "PATH" and install packages from requirements.txt.
```
$ cd ../path/to/QA-Tests-Debugs-GUDLFT-P11
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install -U pip
$ pip install -r requirements.txt
```

Then if you want to browse remotes branches :
```
$ git branch -r | grep -v '\->' | grep -v 'main' | while read remote; do git branch --track "${remote#origin/}" "$remote";
done
```

See all branches :
```
$ git branch
```

Choose a branch-name :
```
$ git checkout <branch-name>
```

## 4. Tests
On __main__ or __QA__ branche :
All documented tests are in "tests" folder.

Use Pytest :
```
$ pytest -vv
```

Use/see Coverage (test, report, html version):
```
$ coverage run -m pytest
$ coverage report -m
$ coverage html
```

Performance test (Locust):
First use flask :
```
$ flask run
```

Then launch locust :
```
$ cd test/performance_test
$ locust
```
__REQUESTED PARAMETERS__ :  
__Number of users(peak concurrency)__
```
6
```
__Spawn rate (users started/second)__
```
1
```
__Host__
```
http://127.0.0.1:5000 
```

## 5. Branches Details
The branches are listed from the most recent to the initial one :

* QA : *Quality assurance*
* locust : *Performance test*
* amelioration/editable_ratio_points_for_place : *functionality asked by mentor*
* error/book_url : __Issues found__ ; *wrong url crash the application*
* func/display-points-avoid-favoritism : *functionality asked* [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/7)
* bug/booking-places-in-past-competitions : [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/5)
* bug/book-no-more-than-12-places : [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/4)
* bug/can-not-book-more-than-available : __Issues found__
* bug/use-more-than-points-allowed : [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/2) and [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/6)
* legacy 
* bug/unknow-email-crash : [issue](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/1)
* main


## 6. Author

Valentin Pheulpin

