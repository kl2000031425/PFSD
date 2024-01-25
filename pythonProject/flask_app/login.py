from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.methods=='POST':
        username=request.form['user']
