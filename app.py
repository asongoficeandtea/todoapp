from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alimatea7:mariam@localhost/datadb'
db = SQLAlchemy(app)

class Task(db.Model):
    task_name = db.Column(db.String(100), primary_key=True)

db.create_all()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.form:
        task = Task(task_name=request.form.get("task_name"))
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
