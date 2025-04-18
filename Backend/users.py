from dbconnection import db #msql,
import prettyprint
import bcrypt

class userProfile:
    def __init__(self):
        self.cursor = db.cursor() #msql.connect().cursor()
        #self.connection = msql.connect()
        self.user_id=None
        self.user_nm=''
        self.address=''
        self.state=''
        self.country='' 
        self.zip=''
        self.contact=''
        self.email=''
        self.password= ''

    def login(self,data):
        usrnm=data['userName']
        # CHECKS IF USERNAME EXSIST
        self.cursor.execute("SELECT user_nm,password FROM productdb.user WHERE user_nm=%s", [usrnm]) 
        #self.cursor.execute(usrQryStr)
        usrQry = self.cursor.fetchall()
        if not usrQry:
            return 400
        #print(usrQry)
        #print(usrQry[0][1])
        storedHash =usrQry[0][1]
        password_bytes = data['password'].encode('utf-8')
        salt =bcrypt.gensalt()
        _hashed_pass = bcrypt.hashpw(password_bytes, salt)
        #print(type(_hashed_pass))
        #print(_hashed_pass)
        #print(type(storedHash))
        #print(storedHash)
        if (bcrypt.checkpw(data['password'].encode('utf-8'), storedHash.encode('utf-8'))):
            #print(True)
            print('We did it......')
            return 200
        else:
            #userReg=self.register(usrData)
            #print(False)
            print('We are failed.....')
            return 404 #userReg
    
    def register(self,data):
        #Do not save password as a plain text
        #_hashed_pass =  hashlib.md5(data['password'].encode('utf8')).hexdigest()
        password_bytes = data['password'].encode('utf-8')
        print('password_bytes = ',password_bytes)
        salt =bcrypt.gensalt()
        print('salt = ',salt)
        _hashed_pass = bcrypt.hashpw(password_bytes, salt)
        print('_hashed_pass = ',_hashed_pass)
        print('\n--------------------------------\n')
        #salt =bytes(bcrypt.gensalt(), 'utf-8')
        #print('Str salt = ',salt)
        #_hashed_pass = bcrypt.hashpw(password_bytes, salt)
        #print('_hashed_pass = ',_hashed_pass)
        usrnm=data['userName']
        firstnm=data['FirstName']
        lstnm=data['LastName']
        email=data['email']
        addrs=data['address']
        city=data['city']
        addrs = addrs + ' ' + city
        sta=data['state']
        cntry=data['country']
        pstlcd=data['postalcode']
        cntc=data['mobile']
        '''if bcrypt.checkpw(password_bytes, _hashed_pass):
            print("It Matches!")
        else:
            print("It Does not Match :(")'''
        self.cursor.execute("SELECT user_nm FROM productdb.user WHERE user_nm=%s", [usrnm]) # CHECKS IF USERNAME EXSIST
        #self.cursor.execute("SELECT COUNT(1) FROM productdb.user WHERE user_nm=%s", [usrnm])
        res=self.cursor.fetchall()
        print(res)
        if res==1: #self.cursor.fetchone()[0]:
            return 501 #'<a href="/signup">User already exist. Please add another userrname</a>'
        else:
            #Save edits
            query="INSERT INTO productdb.user(user_nm,first_nm,last_nm,address,state,country,zip,contact,email,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            res=self.cursor.execute(query,(usrnm,firstnm,lstnm,addrs,sta,cntry,pstlcd,cntc,email,_hashed_pass))
            self.cursor.connection.commit()
        if(res==1):
            return 200
        else:
            return 400