from flask import Flask, render_template, request, flash
from forms import GetProblem 
from dotenv import load_dotenv
import os 



load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



@app.route('/', methods = ['POST', 'GET'])
def home():
    form = GetProblem()
        
    if form.validate_on_submit():
        name = form.username.data
        office = form.office_number.data
        department = form.department.data
        problem = form.problem.data
        
        print(name, office, department, problem)
        flash('FORM SUBMITTED SUCCESSFULY')
        
        
    return render_template('index.html', form = form, )



if __name__ == 'main':
    app.run(debug=True)
    
    