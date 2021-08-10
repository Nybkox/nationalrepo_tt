FROM python:3.9 as builder

WORKDIR /application

COPY . .

# install pipenv
RUN pip install pipenv

# install dependencies
RUN pipenv install --deploy --ignore-pipfile

# create db
RUN pipenv run python create_db.py

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]
