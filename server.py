# -*- coding = utf-8 -*-
# @Time :2021/1/3 7:02 下午
# @Author: XZL
# @File : server.py
# @Software: PyCharm
import datetime
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import *
import json

# Flask web端所有功能封装在server中
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(128)
CORS(app, supports_credentials=True)


@app.route("/raw")
def raw():
    return render_template("ready.html")


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    # 获取表单信息
    s_id = request.form.get('studentID')
    s_name = request.form.get('studentName')
    door = request.form.get('door')
    code_type = request.form.get('codeType')
    time = datetime.datetime.now().strftime('%m-%d %H:%M')
    print(s_name, s_id, door)
    if s_id and s_name is not None:
        # 日志记录
        filehandle = open("log.txt", "a")
        filehandle.write('ID:{} -- Name: {} -- Door: {} T: {}\n'.format(s_id, s_name, door, time))
        filehandle.close()
    # 模板渲染
    student = {'id': s_id, 'name': s_name, 'door': door, 'codeType': code_type}

    session['studentID'] = s_id
    session['studentName'] = s_name
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=14)

    return render_template('index_v2.html', s=student)


@app.route('/checkSession')
def get_session():
    s_id = session.get('studentID')
    s_name = session.get('studentName')
    if s_id and s_name is not None:
        return jsonify({'studentID': s_id, 'studentName': s_name})
    else:
        return jsonify({'error': 1})


if __name__ == '__main__':
    app.run()
