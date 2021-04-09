from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gahDej14b@localhost/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    tasks = db.relationship('Task', backref='user')


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def user():
    if request.form:
        user = User(username=request.form.get("username"))
        db.session.add(user)
        db.session.commit()
    return render_template('user.html')
        
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.form:
        task = Task(task_name=request.form.get("task_name"), user = User.query.filter_by(username).first())
        db.session.add(task)
        db.session.commit()
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@app.route('/update', methods=['GET', 'POST'])
def update():
    new_task = request.form.get("new_task")
    old_task = request.form.get("old_task")
    task = Task.query.filter_by(task_name=old_task).first()
    task.task_name = new_task
    db.session.commit()
    return redirect('/')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    task_name = request.form.get("task_name")
    task = Task.query.filter_by(task_name=task_name).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
