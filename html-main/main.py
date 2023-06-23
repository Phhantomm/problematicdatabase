from flask import Flask, jsonify, redirect, url_for, render_template, request, session, flash
import requests
import json

from flask_sqlalchemy import SQLAlchemy
# import os
# os.system("pip install Flask-SQLAlchemy")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserInfo.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

with app.app_context():
     db.create_all()


# class UserInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(80), nullable=False)
#     lastname = db.Column(db.String(80), nullable=False)
#     number = db.Column(db.Float, nullable=False)

#     def __init__(self, name, surname, telephone):
#         self.name = name
#         self.surname = surname
#         self.telephone = telephone
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


# with app.app_context():
#     db.create_all()
    # b1 = UserInfo(name='shrek', lastname='shrekker', number=679123432)
    # db.session.add(b1)
    # db.session.commit()
    # b7 = UserInfo.query.first()
    # print(b7)
    # all = UserInfo.query.all()
    # b6 = UserInfo.query.get(5)
    # db.session.delete(b6)
    # db.session.commit()
    # idk = UserInfo.query.filter_by(name='shrek').all()
    # for each in all:
    #     print(each)


@app.route('/', methods=['GET','POST'])
def home():


    return render_template('index.html')


@app.route('/product', methods=['GET', 'POST'])
def product():
    # if request.method=='POST':

    #     name = request.form['name']
    #     surname = request.form['surname']
    #     telephone = request.form['telephone']

    #     # # Create a new User object and store it in the database
    #     user = UserInfo(name=name, surname=surname, telephone=telephone)
    #     db.session.add(user)
    #     db.session.commit()
    #     return jsonify({'message': 'Order placed successfully'})

    # Redirect to a success page or perform any other actions
    # return redirect(url_for('product'))

    return render_template('product.html')



@app.route('/user')
def user():

    return render_template('user.html')


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'
@app.route('/youshallnotpass')
def youshouldnthavedonethat():
    return render_template('youshouldnthavedonethat.html')
@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        t = request.form['title']
        a = request.form['author']
        p = request.form['price']

        b1 = UserInfo(title=t, author=a, price=float(p))
        with app.app_context():
            db.session.add(b1)
            db.session.commit()


    return render_template('delivery.html')

# response = requests.get(f'https://api.adviceslip.com/advice')
# result = response.json()
# text = response.text
# with open('advice.json', 'w') as file:
#     file.write(response.text)
#     json.dump(result, file, indent=4)
# s = text.split(" ")
# print(s)
# for i in range(len(s)):
#     l = s[5::1]
    





if __name__ == "__main__":
    app.run(debug=True)