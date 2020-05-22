#!flask/bin/python
#nhady
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask import g, session, redirect, url_for
from flask_simpleldap import LDAP
import json
import os


app = Flask(__name__)

try:
    student_age_file_path  = os.environ['student_age_file_path'] 
except NameError:
    student_age_file_path  = '/data/student_age.json'

student_age_file = open(student_age_file_path, "r")
student_age = json.load(student_age_file)

@app.route('/pozos/api/v1.0/get_student_ages', methods=['GET'])
def get_student_ages():
    return jsonify({'student_ages': student_age })

if __name__ == '__main__':
    app.run()
