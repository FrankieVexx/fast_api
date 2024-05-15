# How to use this code

## fastAPI setup

To run this API, make sure you have Python installed. Then, install FastAPI and uvicorn using pip:

``` bash
pip install fastapi 
pip install uvicorn
```

## Copy this code into a file named fast.py

```python
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {
    1: {
        "name": "Milk",
        "price": 45,
        "brand": "KCC"
    }
}

@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item Id not found.")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists.")
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item Id not found.")
    
    if item.name is not None:
        inventory[item_id]['name'] = item.name
    if item.price is not None:
        inventory[item_id]['price'] = item.price
    if item.brand is not None:
        inventory[item_id]['brand'] = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The Id you would like to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item Id not found.")
    del inventory[item_id]
    return {"Success": "Item deleted successfully"}
```
## Running tha API

To start the server, run this command: uvicorn fast:app --reload
If you opt to use a different app name, ensure you use it in place of "fast" in the command above
You can then access the API at http://localhost:8000 # Use tools like cURL or Postman to explore the endpoints



# Setting up SQLAlchemy Datbase

## Installation

Before running the provided code, make sure you have SQLAlchemy installed. You can install it via pip:

```bash
pip install sqlalchemy
```
## Using the code

Copy the code below and paste in a file named "main.py"

### Import necessary modules from SQLAlchemy
```python
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a class representing the 'companies' table in the database
class Company(Base):
    # Specify the table name
    __tablename__ = "companies"

    # Define columns for the 'companies' table
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    age = Column("Age", Integer)
    ceo = Column("ceo", String)
    marketvalue = Column("marketvalue", Float)

    # Constructor method for Company instances
    def __init__(self, name, age, ceo, marketvalue):
        self.name = name
        self.age = age
        self.ceo = ceo
        self.marketvalue = marketvalue

    # Representation method to display Company instances
    def __repr__(self):
        return f"{self.name} {self.age} {self.ceo} {self.marketvalue}USD"

# Define a class representing the 'employees' table in the database
class Employee(Base):
    # Specify the table name
    __tablename__ = "employees"

    # Define columns for the 'employees' table
    empname = Column("empname", String)
    empid = Column("empid", Integer, primary_key=True, autoincrement=True)
    address = Column("address", String)
    boss = Column(String, ForeignKey("companies.id"))

    # Constructor method for Employee instances
    def __init__(self, empname, empid, address, boss):
        self.empid = empid
        self.empname = empname
        self.address = address
        self.boss = boss

    # Representation method to display Employee instances
    def __repr__(self):
        return f"{self.empname} {self.address} employed by {self.boss}"

# Create an engine to connect to the database
engine = create_engine("sqlite:///mydb.db", echo=True)

# Create the tables defined by Base in the database
Base.metadata.create_all(bind=engine)

#Create a sessionmaker to generate Session instances
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of the Company class and add them to the session
company1 = Company("Marginseye", 4, "Edwin", 150000)
session.add(company1)
session.commit()

#Additional companies can be added similarly

# Querying objects
# Query all Company objects from the database and print the results
results = session.query(Company).all()
print(results)

# Create instances of the Employee class and add them to the session
emp1 = Employee("Els", 1, "Ruaka", "Edwin")
session.add(emp1)
session.commit()
```
This guide provides instructions for installing SQLAlchemy and a step-by-step explanation of the provided code.




