from flask import Flask
from auth.views import FormSignupWithoutVerification


app = Flask(__name__)


app.add_url_rule("/signup", view_func=FormSignupWithoutVerification.as_view("signup"))
