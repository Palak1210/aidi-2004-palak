from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from resources.student import add_student, get_student, edit_student, delete_student
from db import db

import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://QX3sGZ1TVj:ofZiwKGAwS@remotemysql.com:3306/QX3sGZ1TVj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(add_student, '/student')
api.add_resource(get_student, '/student')
api.add_resource(delete_student, '/student')
api.add_resource(edit_student, '/student')

app.run(port=6000, debug=True)
