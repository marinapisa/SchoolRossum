from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Marina-PC\\Documents\\Python\\SchoolRossum\\aplication.sqlite3'
app.config['SECRET_KEY'] = 'rocknaveia'
db = SQLAlchemy(app)


from view import *
if __name__ == '__main__':
    app.run(debug=True)
