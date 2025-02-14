from dbconnection import msql

class Quotes:

    def __init__(self):
        self.cursor = msql.connect().cursor()

    def getQuotes(self):
        self.cursor.execute('select * from stocks')
        aData = self.cursor.fetchall()
        stock_data = []
        content = {}
        for res in aData:
            content = {
                'id' : res[0],
                'client_id' : res[1],
                'stock' : res[2],
                'stock_count' : res[3],
            }
            stock_data.append(content)
            print(content)
            content = {}
        return stock_data
    
    def updateStock(self, data):
        return "Update Stock"