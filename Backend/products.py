from dbconnection import db #msql,
import prettyprint

class Products:
    def __init__(self):
        self.cursor = db.cursor() #msql.connect().cursor()
        #self.connection = msql.connect()

    def getProducts(self):
        #self.cursor.execute("SELECT * FROM product")
        self.cursor.execute("SELECT * FROM product")
        aData = self.cursor.fetchall()
        #final_result = [i[0] for i in aData]
        #for i in aData:
        #   print(i[1])
            
        payload = []
        content = {}
        for result in aData:
            content = {
                'id':result[0],
                'title':result[1],
                'description':result[3],
                'price':result[2]
            }
            payload.append(content)
            content = {}
        return payload
    
    def createProduct(self, data):
        insert_sql = "INSERT INTO productdb.product ( title, price, description) VALUES (%s, %s, %s)"
        values = (data['title'],data['price'],data['description'])
        res=self.cursor.execute(insert_sql,values)
        self.cursor.connection.commit()
        if(res==1):
            return 200
        else:
            return 400
    
    def updateProduct(self, id, data):
        #update_sql ="UPDATE product SET title=%s, price=%s, description=%s where id = %s"
        #values = (data['title'],data['price'],data['description'])
        #set_clause_parts = [f"{column} = ? " for column in data.keys()]
        #set_clause = ", ".join(set_clause_parts)
        set_clause = ", ".join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in data.items()])
        query = f"UPDATE product SET {set_clause} WHERE id = {id}"
        values = list(data.values())
        #values.append(id)
        #self.cursor.execute(query,values)
        res=self.cursor.execute(query)
        #print(self.cursor._last_executed)
        self.cursor.connection.commit()
        if(res==1):
            return 200
        else:
            return 400
    
    def deleteProduct(self, id):
        query = f"DELETE from product WHERE id = {id}"
        res=self.cursor.execute(query)
        self.cursor.connection.commit()
        if(res==1):
            return 200
        else:
            return 400
    
    def getSingleProduct(self, id):
        aData = ''
        query = f"Select * from product WHERE id = {id}"
        self.cursor.execute(query)
        aData = self.cursor.fetchall()
        #self.cursor.connection.commit()
        if(len(aData)>0):
            return aData
        else:
            return None