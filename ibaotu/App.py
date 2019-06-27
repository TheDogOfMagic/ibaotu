# -*- coding: utf-8 -*-

from flask import Flask, flash, url_for, redirect,make_response,Response, get_flashed_messages
from flask import request
from flask import render_template
from spider import get_download_url

from werkzeug.contrib.fixers import ProxyFix  # 生产环境中加入
import requests

app = Flask(__name__) #导入实际文件名才可以根据文件找到模板
app.secret_key = 'some_secret'

@app.errorhandler(404)
def page_not_found(error):
  resp = make_response(render_template('not_found.html'), 404)
  resp.headers['X-Something'] = 'A value'
  return resp

@app.route('/')
def index():
    indexcss = url_for('static', filename='CSS/index.css')
    jqjavascript = url_for('static', filename='JQuery/jquery-3.3.1.js')
    indexjs = url_for('static', filename='JavaScript/index.js')

    return render_template('index.html', indexcss=indexcss, jqjavascript=jqjavascript, indexjs=indexjs)

@app.route('/api/ibaotu')
def ibaotu_api():
    baotu = request.values.get('baotu')
    # print(request.values)
    # pass 判断是否有效的url
    if 'https://ibaotu.com/sucai/' in baotu:
        download_url = get_download_url(baotu)
        print(download_url)
        return download_url
    else:
        return '链接错误，请重新复制链接'

@app.route('/hello')
def hello():
    return 'Hello Flask'

# app.wsgi_app = ProxyFix(app.wsgi_app)  # 生产环境中加入

def main():
    app.run()


__name__ == '__main__' and main()
