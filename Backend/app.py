from flask import Flask,Request,Response,render_template,send_from_directory,jsonify,request
from flask_cors import CORS,cross_origin
import os,sys,datetime
from data import my_list

#import quotes
#static_folder='../frontend/dist'
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    name = request.headers.get("Accept-name","Ankit")
    result = list(map(lambda list_ele:connect_frontend(list_ele,name), my_list))
    valid_result = next((item for item in result if item), name)
    return jsonify(valid_result) #render_template('index.html') 

@app.route('/cap')
def post_cap():
    return jsonify(my_list) #render_template('index.html') 

@app.route('/cap/<int:id>', methods = ['POST'])
def buyer(id):
    data = request.get_json()
    if('price' not in data):
        return jsonify({'messgae': 'please set price of food'}), 400
    price = int(data['price'])
    datalist = next(p for p in my_list if p['id']== id)
    if(price > datalist['amount']):
        return jsonify({'messgae': 'Not enough amount'}), 400
    datalist['amount'] -= price
    return jsonify({'messgae': 'Congratulation, you have enough amount'})

def connect_frontend(list_ele,name):
    result = {}
    for trans in list_ele['trans']:
        if trans['name'] == name:
            result = {
                'id':list_ele['id'],
                'name': trans['name'],
                'age': trans['age'],
                'city': trans['city'],
                'food': trans['food'],
                'amount': list_ele['amount'],
                'status':list_ele['status']
            }
    return result

""" @app.route('/index_data')
def index_data():
    data = {
        'title': 'Welcome to Angular-Python App',
        'message': 'This is an example integration between Angular and Python!'
    }
    if request.method == "POST":
        #data = request.form("blah")
        #print("blah")
        search = request.get_json()
        return jsonify(data)
    return render_template('show-api.component.html') """
#return render_template('show-api.component.html',data = jsonify(data))

#quoteObj = quotes.Quotes()


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