from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

#Em config passamos banco://usuario:senha@host/banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/websiteuser'

#codificacao e decode do code
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#usuario extende o db
class Usuario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    nome = db.Column (db.String(30))
    website = db.Column(db.String(255))
    phone = db.Column (db.String(255))
    user_name = db.Column(db.String(255))
    company =db.Column (db.String(255))

    def to_json(self):
            return {"id": self.id, "email": self.email, "nome": self.nome,"website":self.website,"phone":self.phone,"user_name":self.user_name, "company": self.company } 
