from flask import Flask, request, flash, url_for, redirect, render_template, json
from app import app
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.ProjectManager
login_data=db.login


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('uname') 
        password = request.form.get('password')
        # data = userLogin.query.get(user_name)
        x=login_data.find_one({"uname":user_name})
        if  x!=None:
            pwd=x['password']
            print(user_name,pwd)
        else:
            print("Error")
        if password == pwd:
            if user_name == 'Admin':
                return redirect(url_for('view_progress'))
            else:
                return redirect(url_for('add_details',user_name=user_name))
    return render_template('login.html')


# @app.route('/admin', methods=['GET', 'POST'])
# def view_progress():
#     if request.method == 'POST':
#         return redirect(url_for('add_mem'))
#     data=userLogin.query.all()
#     return render_template('2nd.html',data=data)

# @app.route('/addmember',methods=['GET','POST'])
# def add_mem():
#     if request.method=='POST':
#         user_name= request.form.get('uname')
#         password = request.form.get('psw')
#         user = userLogin(user_name,password)
#         db.session.add(user)
#         db.session.commit()  
#         flash('Record was successfully added')
#         return render_template('3rd.html')
#     return render_template('3rd.html')

# def addtasks(user_name,task_desc):
#     task=tasks(user_name,task_desc)
#     db.session.add(task)
#     db.session.commit()
#     print("Added tasks")

# @app.route('/viewdetails/<user_name>',methods=['GET','POST'])
# def view_details(user_name):
#     user = userDetails.query.filter_by(username=user_name).first()
#     task = tasks.query.filter_by(username=user_name).all()
#     if request.method=='POST':
#         print("POST")
#         if request.form.get("add")=='add':
#             addtasks(user_name,request.form['task_desc'])
#         task = tasks.query.filter_by(username=user_name).all()
#         return render_template('page4.html',user=user,task=task)
#     return render_template('page4.html',user=user,task=task)

# @app.route('/adddetails/<user_name>',methods=['GET','POST'])
# def add_details(user_name):
#     task = tasks.query.filter_by(username=user_name).all()
#     if request.method=='POST':
#         User=userDetails.query.filter_by(username=user_name).first()
#         User.name=request.form['name']
#         User.address=request.form['address']
#         User.ph_no=request.form['phno']
#         User.part=request.form['part']
#         selitems = request.form.getlist("sel_items")
#         print("selected")
#         print(selitems)
#         for s in selitems:
#             d = tasks.query.filter_by(id=s).first()
#             d.status=1
#         db.session.commit()
#         return render_template('team_mem.html',user=User,task=task)
    
#     User = userDetails.query.filter_by(username=user_name).first()
#     if User is not None:
#         return render_template('team_mem.html', user=User,task=task)
        
#     User = userDetails(
#         user_name, " "," "," "," ")
#     try:
#             db.session.add(User)
#             db.session.commit()
#             print('Added successfully')
#             return render_template('team_mem.html', user=User)
#     except:
#             return "Error adding to database"
