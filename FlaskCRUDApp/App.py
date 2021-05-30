from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy, sqlalchemy



app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dave/code/FlaskLab/FlaskCRUDApp/crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name,email,phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee data inserted successfully")

        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)