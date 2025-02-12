from flask import Flask,Request,Response,jsonify
import flask_cors
import os,sys,datetime

import quotes


app = Flask(__name__)

quoteObj = quotes.Quotes()

@app.route("/")
def index():
    return "<p>Hello, Welcome to Audacika Trading App!</p>"

@app.route("/quote")
def quoteStock():
    a = quoteObj.getQuotes()
    
    return jsonify(a)

#@app.route('/', methods = ['GET', 'POST'])
#def index():
#    return render_template("main.html")

#@app.route('/quote', methods = ['GET', 'POST'])
#def home():
#    return render_template("quote.html")



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()