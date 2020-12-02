from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix


from app.main.book.book_controller import api as home_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)


api = Api(app, title='Api Flask Read Book', version='1.0', description='Api todo list of read books', prefix='/api')
api.add_namespace(home_ns, path='/book')