# **ginger** - Agile Driven Project Management


## Setting Up


### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/realpython/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

------------------

## Run with Docker

With **[Docker](https://www.docker.com)**, you can quickly build and run the entire application in minutes :whale:

```shell
# 1. First, clone the repo
$ git clone https://github.com/mtobeiyf/keras-flask-deploy-webapp.git
$ cd keras-flask-deploy-webapp

# 2. Build Docker image
$ docker build -t keras_flask_app .

# 3. Run!
$ docker run -it --rm -p 5000:5000 keras_flask_app
```

Open http://localhost:5000 and wait till the webpage is loaded.

## Local Installation

It's easy to install and run it on your computer.

```shell
# 1. First, clone the repo
$ git clone https://github.com/mtobeiyf/keras-flask-deploy-webapp.git
$ cd keras-flask-deploy-webapp

# 2. Install Python packages
$ pip install -r requirements.txt

# 3. Run!
$ python app.py
```

Open http://localhost:5000 and have fun. :smiley:

## Configuration

The following environment variables are *optional*:

| Name             | Purpose                                          |
|------------------|--------------------------------------------------|
| `APP_NAME`       | The name of the application. i.e Flask Bones     |
| `MAIL_PORT`      | The port number of an SMTP server.               |
| `MAIL_SERVER`    | The hostname of an SMTP server.                  |
| `MEMCACHED_HOST` | The hostname of a memcached server.              |
| `MEMCACHED_PORT` | The port number of a memcached server.           |
| `POSTGRES_HOST`  | The hostname of a postgres database server.      |
| `POSTGRES_PASS`  | The password of a postgres database user.        |
| `POSTGRES_PORT`  | The port number of a postgres database server.   |
| `POSTGRES_USER`  | The name of a postgres database user.            |
| `REDIS_HOST`     | The hostname of a redis database server.         |
| `REDIS_PORT`     | The port number of a redis database server.      |
| `SECRET_KEY`     | A secret key required to provide authentication. |
| `SERVER_NAME`    | The hostname and port number of the server.      |


## Running the App

## Built With

### Backend

- [Flask](https://flask.palletsprojects.com/) - The Python micro framework for building web applications.
- [Mailjet](https://app.mailjet.com/account/setup-guide) - Mail Delivery API (SMTP Tunnel)


#### Database ORM

- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) - Adds SQLAlchemy support to Flask

#### Database Migrations

- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) - SQLAlchemy database migrations for Flask applications using Alembic

#### Form Data Validation

- [Flask-WTF](https://github.com/lepture/flask-wtf) - Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration.

#### Authentication

- [Flask-Login](https://github.com/maxcountryman/flask-login) - Flask user session management

- [Flask-Bcrypt](https://github.com/maxcountryman/flask-bcrypt) - Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application

- [itsdangerous](https://github.com/pallets/itsdangerous) - Various helpers to pass trusted data to untrusted environments.

#### Websockets

- [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) - Socket.IO integration for Flask applications

#### Date & Time

- [Flask-Moment](https://github.com/miguelgrinberg/Flask-Moment) - Formatting of dates and times in Flask templates using moment.js

#### Email

- [Flask-Mail](https://github.com/mattupstate/flask-mail/) - Flask-Mail adds SMTP mail sending to your Flask applications

#### i18n

- [flask-babel](https://github.com/python-babel/flask-babel) - i18n and l10n support for Flask based on Babel and pytz

---

## Project Structure

## Screenshots

## What's next?

## References

## License