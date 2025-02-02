from flask import Blueprint,render_template

route = Blueprint('routes', __name__, template_folder='templates')

@route.route('/')
def index():
    return render_template('index.html')