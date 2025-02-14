from flask import Flask,Request,Response,render_template,send_from_directory
import flask_cors
import os,sys,datetime
#import quotes
#static_folder='../frontend/dist'
app = Flask(__name__) #,static_folder='/static', template_folder='/templates') 

#quoteObj = quotes.Quotes()

@app.route("/")
def index():
    return render_template("index.html")

""" @app.route("/quote")
def quoteStock():
    a = quoteObj.getQuotes()
    
    return jsonify(a) """

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