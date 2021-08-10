# National Repo TT
Solution to the task for the interview. The text of the task can be found in `data/priklad-prijimaci-rizeni-flask.pdf`.

## Prerequisites
Alternatively you can use Docker.
- Python 3.9 or later installed
- Pipenv installed (recommended)

## Installing
The recommended installation method is using `pipenv`.

First, clone the repo and install the dependencies:

    $ git clone https://github.com/Nybkox/nationalrepo_tt.git
    $ cd nationalrepo_tt
    $ pipenv install 

Second, spawn a shell within the virtualenv:

    $ pipenv shell
Third, create a database and fill it with data from `.csv` files.

    $ python create_db.py

## Running
The easiest way to run it is using flask scripts:

    $ pipenv run flask run

Alternatively, you can use the `run_app.py` file:

    $ pipenv shell
    $ python run_app.py

## Swagger
Swagger is available at http://127.0.0.1:5000/.
