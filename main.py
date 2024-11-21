
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Customer
from schemas import CustomerCreate, CustomerResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
  
    # Create a new customer and save to the database.
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@app.get("/customerlist/", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    # Query the database to get all customers
    customers = db.query(Customer).all()
    
    # If no customers found, raise an exception
    if not customers:
        raise HTTPException(status_code=404, detail="No customers found")
    return customers

@app.get("/greeting/")
def welcome():
    return  {"message":"Welcome to test FastAPI"}

@app.get("/varpara/{id}")
def varpara(id):
    return {"message":"id"+" : "+id}
    
@app.get("/multivarpara/{name}/{salary}")
def multivarpara (name,salary):
    return {"name":name, "salary":salary}

@app.get("/multitypepara/{name}/{age}")
def multitypepara(name:str, age:int):
    return {"name": name, "age": age}

