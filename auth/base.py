from flask.views import MethodView
from flask import render_template
from flask import request

from .hashing import hashing_strategy
from .hashing.password import Password
from .validators import validate_string
from .models import User, session


class BaseFormSignup(MethodView):
    methods = ["GET", "POST"]

    def get(self):
        return render_template("signup.html")

    def post(self):
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        username_valid = validate_string(username, self.username_validators)
        email_valid = validate_string(email, self.email_validators)
        password_valid = validate_string(password, self.password_validators)

        if not (username_valid and email_valid and password_valid):
            return render_template(
                "signup_invalid.html",
                username_valid=username_valid,
                email_valid=email_valid,
                password_valid=password_valid
            )

        password = Password(password, hashing_strategy)

        user = User(username=username, email=email, password=password.hashed)

        session.add(user)
        session.commit()

        if self.email_verification_enabled:
            self.email_verifier.verify(email, {"username": username})

        return render_template("signup_success.html", username=username, email=email)
