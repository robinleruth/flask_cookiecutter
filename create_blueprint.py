import os
import sys

if len(sys.argv) != 2:
    print("Please give a bp name as first argument")
    sys.exit()

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(basedir, 'project', 'app')

blueprint_name = sys.argv[1]
blueprint_dir = os.path.join(basedir, blueprint_name)

os.mkdir(blueprint_dir)


blueprint_init_file_name = os.path.join(blueprint_dir, '__init__.py')
with open(blueprint_init_file_name, 'w') as f:
    f.write("from flask import Blueprint\n")
    f.write("from app import db\n")
    f.write("\n")
    f.write("bp = Blueprint('" + blueprint_name + "', __name__)\n")
    f.write("\n")
    f.write("from .import routes\n")
    f.write("from .import models\n")

blueprint_route_file_name = os.path.join(blueprint_dir, 'routes.py')
with open(blueprint_route_file_name, 'w') as f:
    f.write("from . import bp, db\n")
    f.write("from flask import render_template\n")
    f.write("\n")
    f.write("@bp.route('/test')\n")
    f.write("def test():\n")
    f.write("    return render_template('index.html')\n")

blueprint_form_file_name = os.path.join(blueprint_dir, 'forms.py')
with open(blueprint_form_file_name, 'w') as f:
    f.write("from flask_wtf import FlaskForm\n")
    f.write("from wtforms import StringField, PasswordField, SubmitField\n")
    f.write("from wtforms.validators import DataRequired\n")
    f.write("\n")
    f.write("class LoginForm(FlaskForm):\n")
    f.write("    username = StringField('Username', validators=[DataRequired()])\n")
    f.write("    password = PasswordField('Password', validators=[DataRequired()])\n")
    f.write("    submit = SubmitField('Submit')\n")


blueprint_model_file_name = os.path.join(blueprint_dir, 'models.py')
with open(blueprint_model_file_name, 'w') as f:
    f.write("from . import db\n")
    f.write("\n")
    f.write("class User(db.Model):\n")
    f.write("    id = db.Column(db.Integer, primary_key=True)\n")
    f.write("    username = db.Column(db.String(64), index=True, unique=True)\n")
    f.write("    password_hash = db.Column(db.String(128))\n")
    f.write("\n")
    f.write("    def __repr__(self):\n")
    f.write("        return '<User {}>'.format(self.user)\n")
