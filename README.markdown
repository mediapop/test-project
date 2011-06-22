Install instructions (these are for Linux or OSX):
==================================================

You'll need python, git, mysql, distutils, setuptools, pip and virtualenv installed.

* http://www.python.org/download/releases/2.7.1/
* http://git-scm.com/download
* http://www.mysql.com

You'll need a mysql user called perfs with a password of perfs and a database called perfs

    mkdir django-project
    cd django-project
    virtualenv --no-site-packages perfsys
    cd perfsys/bin && source activate && cd ../../

    # begin installing lbiraries needed for project to run
    git clone https://github.com/mediapop/mplib.git
    git clone https://github.com/mediapop/django-paypal.git && cd django-paypal && python setup.py build && python setup.py install && cd ..
    git clone https://github.com/mediapop/Django-SQS.git
    git clone https://github.com/hmarr/django-ses.git && cd django-ses && python setup.py build && python setup.py install && cd ..
    git clone https://github.com/dcramer/django-sentry.git && cd django-sentry && python setup.py build && python setup.py install && cd ..
    git clone https://github.com/django-debug-toolbar/django-debug-toolbar && cd django-debug-toolbar && python setup.py build && python setup.py install && cd ..
    wget http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz/download && tar -xvf MySQL-python-1.2.3.tar.gz && cd MySQL-python-1.2.3 && python setup.py build && python setup.py install && cd ..
    git clone https://github.com/facebook/python-sdk.git && cd python-sdk && python setup.py build && python setup.py install && cd ..

    git clone https://github.com/mediapop/test-project.git

    cd test-project/src/perfsystems
    python manage.py syncdb && python manage.py runserver

You should now be able to view the test site at http://127.0.0.1:8000

