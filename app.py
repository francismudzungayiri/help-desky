from flask import Flask, render_template, request, flash
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
        
        
    return render_template('index.html', form = form, )



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LogIn()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    return render_template('login.html', form = form) 






if __name__ == 'main':
    app.run(debug=True)
    
    