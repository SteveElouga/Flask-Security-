import os
from flask_sqlalchemy import SQLAlchemy
from FlaskSecurity import app
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import logging as lg


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.Text(), nullable = False)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    

@app.cli.command()
def init_db():  
    db.drop_all() 
    db.create_all()
    lg.warning('Database initialized!')
        