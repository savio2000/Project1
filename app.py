
from multiprocessing import connection
from pdb import post_mortem
from pickle import GET
import sqlite3
from flask import Flask, make_response,render_template, request,make_response
app=Flask(__name__)

@app.route('/qs')
def hello_world():
    kk=make_response(order)
        
    return kk 
   

@app.route("/")
def home():
    return render_template("home.html")  
@app.route("/home.html")
def home1():
    return render_template("home.html")      

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        connection=sqlite3.connect("user_data.db")
        cursor=connection.cursor()
        name=request.form['name']
        password=request.form['password']
        q="SELECT name,password from login_data where name='"+name+"' and password='"+password+"' "
        cursor.execute(q)
        res=cursor.fetchall()
        if len(res)>0:
            return render_template("home.html")
        else:
            print("sorry")    

    return render_template("login.html")  

@app.route("/method", methods=['GET','POST'])
def method():
    if request.method=='GET':
        print("get anu mone") 
    else:
        return 'get alla kutta' 
    return render_template("login.html")        

if __name__=='__main__':
    app.run(debug=True)    