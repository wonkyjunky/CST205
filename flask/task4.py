from flask import Flask, render_template 
from flask_wtf import FlaskForm

result = [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]

app = Flask(__name__,	
			static_url_path='',	
			static_folder='static',
            template_folder='templates')

@app.route('/')
def hello1():
 return render_template('hello.html') 

@app.route('/templates')
def hello2():
 return render_template('color.html',result=result) 
