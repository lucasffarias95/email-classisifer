from flask import render_template, Blueprint

web = Blueprint('main', __name__)

@web.route('/')
def index():
    return render_template('index.html')