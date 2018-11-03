import os
import venv

project_name = "project"

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(basedir, project_name)

os.mkdir(basedir)

venv_dir = os.path.join(basedir, 'venv')
# venv.create(venv_dir)
INDENT = "    "

app_directory = os.path.join(basedir, 'app')
os.mkdir(app_directory)

app_init_file_name = os.path.join(app_directory, '__init__.py')
app_route_file_name = os.path.join(app_directory, 'routes.py')
with open(app_init_file_name, 'w') as f:
    f.write("from flask import Flask\n")
    f.write("# from flask_bootstrap import Bootstrap\n")
    f.write("# from flask_nav import Nav\n")
    f.write("# from flask_migrate import Migrate\n")
    f.write("# from flask_sqlalchemy import SQLAlchemy\n")
    f.write("# from flask_admin import Admin\n")
    f.write("\n")
    f.write("from config import ProdConfig\n")
    f.write("import logging\n")
    f.write("from logging.handlers import SMTPHandler, RotatingFileHandler\n")
    f.write("import os\n")
    f.write("\n")
    f.write("# bootstrap = Bootstrap()\n")
    f.write("# nav = Nav()\n")
    f.write("# migrate = Migrate()\n")
    f.write("# db = SQLAlchemy()\n")
    f.write("# admin = Admin()\n")
    f.write("\n")
    f.write("\n")
    f.write("def create_app(config=None):\n")
    f.write("    app = Flask(__name__)\n")
    f.write("    app.config.from_object(config)\n")
    f.write("    # app.register_blueprint(bp)\n")
    f.write("    # bootstrap.init_app(app)\n")
    f.write("    # nav.init_app(app)\n")
    f.write("    # db.init_app(app)\n")
    f.write("    # migrate.init_app(app, db)\n")
    f.write("    # admin.init_app(app)\n")
    f.write("\n")
    f.write("    # if not app.debug:\n")
    f.write("    #     if app.config['MAIL_SERVER']:\n")
    f.write("    #         auth = None\n")
    f.write("    #         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:\n")
    f.write("    #             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])\n")
    f.write("    #         secure = None\n")
    f.write("    #         if app.config['MAIL_USE_TLS']:\n")
    f.write("    #             secure = ()\n")
    f.write("    #         mail_handler = SMTPHandler(mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),\n")
    f.write("    #                                     fromaddr='no-reply@' + app.config['MAIL_SERVER'],\n")
    f.write("    #                                     toaddrs=app.config['ADMINS'],\n")
    f.write("    #                                     credentials=auth,\n")
    f.write("    #                                     secure=secure)\n")
    f.write("    #         mail_handler.setLevel(logging.ERROR)\n")
    f.write("    #         app.logger.addHandler(mail_handler)\n")
    f.write("\n")
    f.write("    if not os.path.exists('logs'):\n")
    f.write("            os.mkdir('logs')\n")
    f.write("    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)\n")
    f.write("    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))\n")
    f.write("    file_handler.setLevel(logging.INFO)\n")
    f.write("    app.logger.addHandler(file_handler)\n")
    f.write("    app.logger.setLevel(logging.INFO)\n")
    f.write("    app.logger.info('start up')\n")
    f.write("\n")
    f.write("\n")
    f.write("    return app\n")
    f.write("\n")
    f.write("app = create_app(ProdConfig)\n")
    f.write("\n")
    f.write("from app import routes\n")

with open(app_route_file_name, 'w') as f:
    f.write("from app import app\n")
    f.write("# from app import nav\n")
    f.write("# from flask.nav.elements import Navbar, View\n")
    f.write("\n")
    f.write("# @nav.navigation()\n")
    f.write("# def top():\n")
    f.write("    # return Navbar('MySite', View('Index', 'index'))\n")
    f.write("\n")
    f.write("@app.route('/')\n")
    f.write("def index():\n")
    f.write("    return render_template('index.html')\n")


config_file_name = os.path.join(basedir, 'config.py')
with open(config_file_name, 'w') as f:
    f.write("import os\n")
    f.write("\n")
    f.write("\n")
    f.write("basedir = os.path.abspath(os.path.dirname(__file__))\n")
    f.write("\n")
    f.write("\n")
    f.write("class Config:\n")
    f.write("    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'\n")
    f.write("    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')\n")
    f.write("    # SQLALCHEMY_TRACK_MODIFICATIONS = False\n")
    f.write("    STATIC_FOLDER = os.path.join(basedir, 'app', 'static\n")
    f.write("    # MAIL_SERVER = ""\n")
    f.write("    # MAIL_PORT = ""\n")
    f.write("    # MAIL_USE_TLS = ""\n")
    f.write("    # MAIL_USERNAME = ""\n")
    f.write("    # MAIL_PASSWORD = ""\n")
    f.write("\n")
    f.write("class ProdConfig(Config):\n")
    f.write("    pass\n")
    f.write("\n")
    f.write("class TestConfig(Config):\n")
    f.write("    Testing = True\n")
    f.write("    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'temp.db')\n")

run_file_name = os.path.join(basedir, 'application.py')
with open(run_file_name, 'w') as f:
    f.write("from app import app\n")
    f.write("\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    app.run()\n")

template_directory = os.path.join(app_directory, 'templates')
os.mkdir(template_directory)
static_directory = os.path.join(app_directory, 'static')
os.mkdir(static_directory)

base_template_file_name = os.path.join(template_directory, 'base.html')
with open(base_template_file_name, 'w') as f:
    f.write("{#\n")
    f.write("{% extends 'bootstrap/base.html' %}\n")
    f.write("{% import 'bootstrap/wtf.html' as wtf %}\n")
    f.write("#}\n")
    f.write("\n")
    f.write("{% block title %}\n")
    f.write("Title\n")
    f.write("{% endblock %}\n")
    f.write("\n")
    f.write("{% block content %}\n")
    f.write("<div class='container'>\n")
    f.write("    {% with messages = get_flashed_messages() %}\n")
    f.write("    {% if messages %}\n")
    f.write("    {% for message in mesages %}\n")
    f.write("    <div class='alert alert-info' role='alert'>\n")
    f.write("    {{ message }}\n")
    f.write("    </div>\n")
    f.write("    {% endfor %}\n")
    f.write("    {% endif %}\n")
    f.write("    {% endwith %}\n")
    f.write("</div>\n")
    f.write("{% block app_content %}\n")
    f.write("{% endblock %}\n")
    f.write("{% endblock %}\n")

index_template_file_name = os.path.join(template_directory, 'index.html')
with open(index_template_file_name, 'w') as f:
    f.write("{% extends 'base.html' %}\n")
    f.write("\n")
    f.write("{% block app_content %}\n")
    f.write("<h1>Index</h1>\n")
    f.write("{% endblock %}\n")