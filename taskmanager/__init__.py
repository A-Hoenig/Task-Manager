# remember to pip3 install flask==2.2.5 (newest version throws an error)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# only import on local install if env.py is avaiable
if os.path.exists("env.py"):
    import env  # noqa

# create instance of imported Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create instance of SQLAlchemy class
db = SQLAlchemy(app)

# import last as app and db variables needed
from taskmanager import routes  # noqa