# flask_tracking/auth.py
from flask import Flask
from flask.ext.login import LoginManager

from flask_tracking.users.models import User

login_manager = LoginManager()

login_manager.login_view = "users.login"
# We have not created the users.login view yet
# but that is the name that we will use for our
# login view, so we will set it now.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
	app.run()
