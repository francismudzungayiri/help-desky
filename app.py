from bson import ObjectId
from flask import Flask, render_template, request, flash,redirect, url_for, session
import forms as forms
from dotenv import load_dotenv
import os 
from standalone import ticketing
from pymongo import MongoClient
from flask_session import Session
from flask_bcrypt import Bcrypt
from datetime import date




load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
bcrypt = Bcrypt(app)



#set up the mongodb conection
client = MongoClient('localhost', 27017) 
db = client['Help-Desky'] 
querries_collection = db['querries'] # querries collection
users_collection = db['users']


def current_date():
    today = date.today()
    current = today.strftime("%d %b %Y")
    
    
    return current
    

@app.route('/', methods = ['POST', 'GET'])
def home():
    form = forms.GetProblem()
    
    if form.validate_on_submit():
        name = form.username.data
        office = form.office_number.data
        department = form.department.data
        problem = form.problem.data
        
        ticket_number = ticketing()
        
        data = {
            'name':name,
            'office_number': office,
            'department': department,
            'problem_faced': problem,
            'ticket': ticket_number,
            'status': 'Pending'
        }
        
        querries_collection.insert_one(data)

        
        flash('Thank you, Please Wait for IT to assign a person to help you. ')
        
        
    return render_template('index.html', form = form, title= 'Home' )



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LogIn()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        #check if email and password match
        user = users_collection.find_one({'email': username})
        if user:
            details = user
            passcode = details['password']
            verify_password = bcrypt.check_password_hash(passcode, password)
            
            if verify_password:
                
                session['name'] = details['first_name']
                session['system_role'] = details['system_role']
                username = session.get('name')
                return redirect( url_for('dashboard', username = username))
        
        else:
            flash('User not found.')
                
        
    return render_template('login.html', form = form ) 



@app.route('/dashboard/<username>')
def dashboard(username):
    username = session.get('name')
    role = session.get('system_role')
    res_progress_list = []
    res_progress = 'NOTHING TO SHOW'
    
    global count_pending
    global count_inProgress
    global count_completed
    
    pending_queries =  {'status': 'Pending'}
    if role == 'General User':
        in_progress = {'$and': [{'status': 'In Progress'},{'assigned_to':username}]}    
        res_progress = querries_collection.find(in_progress)
        
        count_inProgress = querries_collection.count_documents(in_progress)
        
        pending = {'$and': [{'status':'Pending'},{'assigned_to':username}]}
        count_pending = querries_collection.count_documents(pending)
        
        completed = {'$and':[{'status':'Completed'}, {'assigned_to': username}]}
        count_completed = querries_collection.count_documents(completed)
    
    else:
        
        count_inProgress = querries_collection.count_documents({'status':'In Progress'})
        count_pending = querries_collection.count_documents({'status':'Pending'})
        count_completed = querries_collection.count_documents({'status':'Completed'})
        
            
    
    res_pending = querries_collection.find(pending_queries)
   
    
    form = forms.NewUser()  
    res_progress_list = list(res_progress)
    
    current_Date = current_date()
    
         
    return render_template(
        'dashboard.html',
        username = username,
        all_pending_queries = res_pending,
        all_inprogress_queries = res_progress_list,
        form = form,
        current_Date = current_Date, 
        pending = count_pending,
        progress = count_inProgress,
        completed = count_completed
    )
    
    
@app.route('/addnewuser', methods=['POST'])
def addNewUser():
    
    form = forms.NewUser()
 
    if form.validate_on_submit():
        firstname = form.firstname.data 
        surname = form.surname.data
        email = form.useremail.data
        system_role =  form.system_role.data
        position =  form.position.data
        password =  form.password.data
        
        hashed_password = bcrypt.generate_password_hash(password)

        new_user = {
            'first_name':firstname,
            'last_name':surname,
            'email':email,
            'system_role':system_role,
            'position':position,
            'password':hashed_password
        }
        
        users_collection.insert_one(new_user)
        user = session.get('name')
        
    return redirect(url_for('dashboard',username = user))



@app.route('/dashboard/<username>/<id>')
def row_details(username, id): 

    form = forms.Assign_Query()
    completeTask = forms.Commplete_Task()
    
    pending_condition =  {'status': 'Pending'}
    progress_condition = {'$and':[{'status':'In Progress'},{'assigned_to': username}]}
    role = session.get('system_role')
    username = session.get('name')


    res =None
    query = None
    if role== 'Administrator':    
        res = querries_collection.find(pending_condition)
        query = next((query for query in res if query['_id'] == ObjectId(id)), None)
    else:
        res = querries_collection.find(progress_condition)
        query = next((query for query in res if query['_id'] == ObjectId(id) ), None)

    
    if query:    
        return render_template('table_row.html', username = username, query = query, form=form, complete_task = completeTask )


@app.route('/assign-pending-query', methods=['POST'])
def assign_query():
    form  = forms.Assign_Query()
    
    if form.validate_on_submit():
        
        assigned_to = form.assign_to.data 
        id = form.id.data
        
        doc_id = ObjectId(id)
        new_data = {
            'assigned_to': assigned_to,
            'status': 'In Progress'
        }
        
        querries_collection.update_one(
            {'_id': doc_id},
            {'$set':new_data }
        )
        
        print('DATA UPDATED SUCCESFULLY')
        
        user = session.get('name')
        return redirect(url_for('dashboard', username=user))
    else:
        print(form.errors)
        return 'NOTHING DONE'
        
        
@app.route('/completed-query', methods = ['POST'])
def complete_task():
    user = session.get('name')
    form = forms.Commplete_Task()
    
    if form.validate_on_submit():
        comment = form.comment.data
        ticket_id = form.id.data
        
        doc_id = ObjectId(ticket_id)
        
        new_data = {
            'status': 'Completed',
            'comment' : comment,
        }
        
        querries_collection.update_one(
            {'_id': doc_id},
            {'$set': new_data}
        )
        print('DATA UPDATED SUCCESFULY')
        return redirect(url_for('dashboard', username=user))
    else:
        print(form.errors)
        return 'ERROR ---- NOTHING UPDATED'
        
    



@app.route('/logout')
def logout():
    session['name'] = None
    session['system_role'] = None
    
    return redirect('/')


if __name__ == 'main':
    app.run(debug=True)
    
    