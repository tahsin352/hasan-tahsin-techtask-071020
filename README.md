# Flask Recipe API

Simple REST-ful-ish api built in flask; built as a project to see recpies and tests the basics of CI, as well as to create a project to use for using docker for flask apps.

Contains a collection of recipes, and supports GET requests. Includes **continuous integration** with **Travis CI** and has a full suite of tests with **PyTest**.

---

#### Installation
```shell
pip install pipenv  # if not already installed
pipenv install
```

#### To Run
```shell
export FLASK_APP=app.py
export FLASK_ENV=production
pipenv run flask run
```

**Run Docker**
Go to the project directory (in where your Dockerfile is, containing your app directory)
Build your Flask image:
```shell
docker build -t myimage .
```
Run a container based on your image:
```shell
docker run -d --name mycontainer -p 5000:5000 myimage
```

#### Tests

To run all pytest tests from the project's root directory:
```shell
pipenv run python -m pytest
```

Tests were written based on [this official flask guide.](https://flask.palletsprojects.com/en/1.1.x/testing/)

#### Other Useful Commands

```shell
pipenv shell			# activate virtual environment
(env)$ exit				# exit current virtual environment
