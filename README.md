# LMNOP

## Live Music Notes, Opinions, Photographs

### Pre-requisites

Install Postgres, create a database called LMNOP. Create a user called LMNOP and grant this user privileges on the LMNOP database. Set an environment variable LMNOP_DB_PW with the LMNOP user's password. 

### To install

1. Create and activate a virtual environment. Use Python3 as the interpreter. Suggest locating the venv/ directory outside of the code directory.

2. pip install -r requirements.txt

3. python manage.py makemigrations lmn

4. python manage.py migrate

5. python manage.py runserver

Site at

127.0.0.1:8000

### Create superuser


`python manage.py createsuperuser`

enter username and password

will be able to use these to log into admin console at

127.0.0.1:8000/admin


### Run tests

To run tests  (some currently fail - see Issues)

```
python manage.py test lmn.tests
```

Or just some of the tests,

```
python manage.py test lmn.tests.test_views
python manage.py test lmn.tests.test_views.TestUserAuthentication
python manage.py test lmn.tests.test_views.TestUserAuthentication.test_user_registration_logs_user_in
```


### Functional Tests with Selenium

Install (upgrade to the latest version if you already have it) Firefox browser. It works best for automated functional testing with Selenium.

Make sure you have the latest version of Chrome, and the most recent chromedriver, and latest Selenium.

geckodriver needs to be in path or you need to tell Selenium where it is. Pick an approach: http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

If your DB is at AWS, your tests might time out, and you might need to use longer waits http://selenium-python.readthedocs.io/waits.html

Start your server with `python manage.py runserver` and then

```
python manage.py test lmn.tests.functional_tests
```

Or select tests, for example,
```
python manage.py test lmn.tests.functional_tests.HomePageTest
python manage.py test lmn.tests.functional_tests.BrowseArtists.test_searching_artists
```


### Test coverage

From directory with manage.py in it,

```
coverage run --source='.' manage.py test lmn.tests

coverage report
```


### PostgreSQL

A local PostgreSQL server will be faster than a AWS one.
https://github.com/DjangoGirls/tutorial-extensions/tree/master/en/optional_postgresql_installation

Internet will have more recent instructions for installing PostgreSQL, start there.

Set admin password, remember it.

Start postgres running

(Run `su postgres` if on a mac/linux)

`pg_ctl start`  enter username and password


start postgres shell with `psql`

And create a user called lmnop

```
create user lmnop with password 'password_here';
```

create a database lmnop

```
create database lmnop owner lmnop;
```

Various postgres shell commands

`\c lmnop`  connect to lmnop database

`\dt`  shows tables

`\d table_name`   shows info (and constraints) for a table
other sql as expected

postgres shell command cheatsheet - https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

set environment variable called `LMNOP_DB_PW`
with a value of the lmnop user's password

For tests, the DB user who is running the tests needs CREATEDB permission, so run

```
ALTER USER lmnop CREATEDB;
```

Mac users may need to run these commands; these one time

```
sudo ln -s /Library/PosgreSQL/10/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PosgreSQL/10/lib/libcrypto.1.0.0.dylib /usr/local/lib`
```

And this when you start a new shell; or set it permanently in .bash_profile

`export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/9.5/lib:$DYLD_LIBRARY_PATH`
