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

    def login(self,userData):
        usrQry= f"select * from user WHERE name = {userData}"
        self.cursor.execute(usrQry)
        usrQry = self.cursor.fetchall()
        nameLst = list()
        final_result = [i[1] for i in usrQry]
        if(usrQry in final_result):
            return 'You are here in login'
        else:
            userReg=self.register(userData)
            return userReg
    
    def register(self,username,password):
        #Do not save password as a plain text
        #_hashed_pass =  hashlib.md5(password.encode('utf8')).hexdigest()
        password_bytes = password.encode('utf-8')
        _hashed_pass = bcrypt.hashpw(password_bytes, bcrypt.gensalt(14))
        if bcrypt.checkpw(password_bytes, _hashed_pass):
            print("It Matches!")
        else:
            print("It Does not Match :(")
        res=self.cursor.execute("SELECT COUNT(1) FROM productdb.user WHERE user_nm = %s;", [username]) # CHECKS IF USERNAME EXSIST
        if self.cursor.fetchone()[0]:
            return '<a href="/signup">User already exist. Please add another userrname</a>'
        else:
            #Save edits
            query="INSERT INTO productdb.user(user_nm,password) VALUES(%s,%s)"
            res=self.cursor.execute(query,(username, _hashed_pass))
            #db.commit()
            self.cursor.connection.commit()
        if(res==1):
            return 200
        else:
            return 400