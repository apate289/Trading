from flask import Flask,Request,Response,render_template,send_from_directory,jsonify,request
from flask_cors import CORS,cross_origin
import os,sys,datetime,pika,json
from data import my_list
import products
from RabbitMQ.rabbitmq import RabbitMQ
import sys

def callback(ch, method, properties, body):
    print(f"Received message: {body}")
#import quotes
#static_folder='../frontend/dist'

pobj=products.Products()
rabbitmq = RabbitMQ()
app = Flask(__name__)
cors = CORS(app)
CORS_ORIGINS = ['http://localhost:5000', 'http://127.0.0.1:4200']
app.config['CORS_HEADERS'] = 'Content-Type'
queue_name = 'test_queue_2'
#rabbitmq.(queue=queue_name)


@app.route('/')
@cross_origin()
def index():
    name = request.headers.get("Accept-name","Ankit")
    result = list(map(lambda list_ele:connect_frontend(list_ele,name), my_list))
    valid_result = next((item for item in result if item), name)
    return jsonify(valid_result) #render_template('index.html')
    #return render_template('index.html') 

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

@app.route('/product', methods = ['GET','POST'])
@cross_origin(origins="*",headers=['Content-Type'])
def productList():
    if(request.method =='GET'):
        data=pobj.getProducts()
        if(len(data)):
            response = jsonify ({
                "result" : data,
                "status":200
            })
        else:
            response = jsonify ({
                "result" : None,
                "status":400
            })
        return response
    elif(request.method =='POST'):
        data=request.json
        aData=pobj.createProduct(data)
        #if(len(data)>0):
        if(aData==200):
            response = jsonify({
                "result" : data,
                "status":200,
                "message":"created successfully"
            })
        else:
            response = jsonify ({
                "result" : None,
                "status":400,
                "message":"failed to create"
            })
        return response
    
@app.route('/product/<int:pid>', methods = ['GET','PUT','DELETE','PATCH','OPTION'])
@cross_origin(origins="*",headers=['content-type'])
def changeproductlist(pid):
    if(request.method =='PUT'):
        data=request.json
        aData=pobj.updateProduct(pid,data)
        if(aData == 200):
            response = jsonify({
                "result" : aData,
                "status":200,
                "message":"updated successfully"
            })
        else:
            response = jsonify({
                "result" : aData,
                "status":400,
                "message":"Updating failed"
            })
        return response
    elif(request.method =='DELETE'):
        aData=pobj.deleteProduct(pid)
        if(aData == 200):
            response = jsonify({
                "result" : aData,
                "status":200,
                "message":"Delete action successfully"
            })
        else:
            response = jsonify({
                "result" : aData,
                "status":400,
                "message":"Delete action failed"
            })
        return response
    elif(request.method =='PATCH'):
        response = jsonify ({
            "result" : None,
            "status":400,
            "message":"failed to Patch"
        })
        return response
    elif(request.method =='GET'):
        aData=pobj.getSingleProduct(pid)
        if(aData != None):
            response = jsonify({
                "result" : aData,
                "status":200,
                "message":"Get single product successfully"
            })
        else:
            response = jsonify({
                "result" : aData,
                "status":400,
                "message":"Get single product failed"
            })
        return response
    else:
        return "Option HTTP method"
    
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '')
    
    # Publish the message to the queue
    rabbitmq
    rabbitmq.publish(queue_name, message=json.dumps({'message': message}))
    return jsonify({'status': 'message sent'})


'''
@app.route('/create')
def createProductList():
    data=pobj.createProduct()
    return jsonify(data)

@app.route('/update')
def updateProductList():
    data=pobj.updateProduct()
    return jsonify(data)'
    '''

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