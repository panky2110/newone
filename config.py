from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.template_folder = 'templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/rest'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/rest12'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
db = SQLAlchemy(app)
Testing=True
app.secret_key = 'super secret key'
