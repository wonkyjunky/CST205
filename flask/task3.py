from flask import Flask, render_template 

app = Flask(__name__,	
			static_url_path='',	
			static_folder='static',
            template_folder='templates')

@app.route('/')
def hello():
	return "Hello World - home page"

@app.route('/templates')
def hello2():
 return render_template('hello.html')