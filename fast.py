from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price:float
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

@app.get("/")
def index():
    return {"Data": "Test"}


@app.get("/about")
def about():
    return {"Data": "About"}

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
    
    if item.name != None:
        inventory[item_id]['name'] = item.name
    if item.price != None:
        inventory[item_id]['price'] = item.price
    if item.brand != None:
        inventory[item_id]['brand'] = item.brand
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(...,description="The Id you would like to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item Id not found.")
    del inventory[item_id]
    return {"Success": "Item deleted successfully"}
