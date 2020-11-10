# Otusapp CRUD

## How to launch on your local machine
* `virtualenv -p python3.8 env`;
* `source env/bin/activate`;
* `pip install -r requirements.txt`;
* `export FLASK_APP=application`;
* `export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{dbuser}:{dbpassword}@{host}:{port}/{dbname}` (specify your database uri);
* `flask db revision "name of revision"`;
* `flask db upgrade`;
* `flask run` or `python wsgi.py`.

## How to build and push a docker image
* `docker build . -t rksalov/otusapp:{tagname}`
* `docker push rksalov/otusapp:{tagname}`
