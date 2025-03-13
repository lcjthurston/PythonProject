from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# configuration for mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///site.db'

# Create instance of SQLAlchemy
db = SQLAlchemy(app)

# Models



@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()