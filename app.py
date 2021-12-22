import sys
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다. OOO입니다.")
#1-1
@app.route('/<user>')
def hello(user):
    return '<h1> hello ' + user
 
#2
@app.route("/about")
def about():
    return render_template('busan1.html', subject="부산중위연령시각화")
 
#3
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/1.jpg') 

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)