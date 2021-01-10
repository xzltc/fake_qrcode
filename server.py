# -*- coding = utf-8 -*-
# @Time :2021/1/3 7:02 下午
# @Author: XZL
# @File : server.py
# @Software: PyCharm
import os

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import *
import json

# Flask web端所有功能封装在server中
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/raw")
def raw():
    return render_template("ready.html")


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    s_id = request.form.get('studentID')
    s_name = request.form.get('studentName')
    print(s_name, s_id)

    filehandle = open("log.txt", "a")
    filehandle.write('ID:{} --- Name: {} \n'.format(s_id, s_name))
    filehandle.close()

    student = {'id': s_id, 'name': s_name}
    return render_template('index.html', s=student)


if __name__ == '__main__':
    app.run()
