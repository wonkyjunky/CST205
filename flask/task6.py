from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

result = {"audio" : ["flac", "m4a", "mp3", "wav", "ogg", "aiff"],"image" : ["jpeg", "gif", "tiff", "png", "svg"]
        }
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

class ArtistList(FlaskForm):
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Click')

artistlist = []

def store_artist(my_artist):
    artistlist.append(dict(
        artistname = my_artist,
        date = datetime.today()
    ))

@app.route('/', methods=['GET','POST'])
def index():
    form = ArtistList()
    if form.validate_on_submit():
        store_artist(form.artist_name.data)
        print(artistlist)
        return redirect('/al')
    return render_template('index.html', form=form)

@app.route('/al')
def al():
    return render_template('al.html', artistlist=artistlist)

@app.route('/colordict')
def hello2():
 return render_template('hello.html',result=result) 
