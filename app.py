from flask import Flask, render_template, request, flash,redirect, url_for
import forms as forms
from dotenv import load_dotenv
import os 



load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



@app.route('/', methods = ['POST', 'GET'])
def home():
    form = forms.GetProblem()
        
    if form.validate_on_submit():
        name = form.username.data
        office = form.office_number.data
        department = form.department.data
        problem = form.problem.data
        
        print(name, office, department, problem)
        flash('FORM SUBMITTED SUCCESSFULY')
        
        
    return render_template('index.html', form = form, title= 'Home' )



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LogIn()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        return redirect( url_for('admin_dashboard', name=username))
        
    return render_template('login.html', form = form ) 


@app.route('/dashboard/<name>')
def admin_dashboard(name):
    return render_template('dashboard.html')





if __name__ == 'main':
    app.run(debug=True)
    
    