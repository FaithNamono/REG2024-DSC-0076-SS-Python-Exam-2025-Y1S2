from app.extensions import db
from datetime import datetime
class Category(db.Model):
    __tablename__= "categories"
    id = db.column(db.integer,primary_key=True)
    name=db.column(db.string(30),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())  
    updated_at = db.Column(db.DateTime, onupdate=datetime.now() )  
    
    def __init__(self, name, description):
        self.name = name  
        self.description = description  

class Product(db.Model):
    __tablename__= "products"
    id = db.column(db.integer,primary_key=True)
    name=db.column(db.string(30),nullable=False)
    price= db.column(db.integer,nullable= False)
    stock=db.column(db.integer,nullable=False)
    color=db.column(db.string(30),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())  
    updated_at = db.Column(db.DateTime, onupdate=datetime.now() )  
    
    def __init__(self, name, price,stock,color):
        self.name = name  
        self.price=price
        self.stock=stock
        self.color=color

class Customer(db.Model):
    __tablename="customers"
    id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(30), nullable=False)  
    last_name = db.Column(db.String(30), nullable=False)  
    contact = db.Column(db.String(15), unique=True, nullable=False)  
    email = db.Column(db.String(100), unique=True, nullable=False)    
    address = db.Column(db.String(255), nullable=True)   
    created_at = db.Column(db.DateTime, default=datetime.now())  
    updated_at = db.Column(db.DateTime, onupdate=datetime.now() )  
    
    def __init__(self, first_name, last_name, contact, email, address):
        self.first_name = first_name  
        self.last_name = last_name  
        self.contact = contact  
        self.email = email  
        self.address=address