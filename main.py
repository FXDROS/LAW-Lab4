from fastapi import FastAPI, status, HTTPException, Depends, Request
from pydantic import BaseModel, Field
from database import SessionLocal
from typing import List, Optional
import models
import uvicorn

app = FastAPI()
db = SessionLocal()

class Item(BaseModel):
    name: str
    price: int
    stock: int

    class Config:
        orm_mode = True

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None

@app.post('/item/create', response_model = Item, status_code = status.HTTP_201_CREATED)
def createItem(item: Item):
    new_item = models.Item(
        name = item.name,
        price = item.price,
        stock = item.stock,
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.get('/item/all-item', status_code = status.HTTP_200_OK)
def getAllItem():
    all_item = db.query(models.Item).all()

    return all_item

@app.get('/item/{item_id}', response_model = Item, status_code = status.HTTP_200_OK)
def getItemById(item_id: str):
    item_id = int(item_id)
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()

    if item is None:
        raise HTTPException(status_code = 404, detail = "Item's not found")

    return item

@app.put('/item/update/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def updateItem(item_id: str, item: UpdateItem):
    item_id = int(item_id)
    update_item = db.query(models.Item).filter(models.Item.item_id == item_id).first()

    if update_item is None:
        raise HTTPException(status_code = 404, detail = "Item's not found")

    if (item.name):
        update_item.name = item.name

    if (item.price):
        update_item.price = item.price

    if (item.stock):
        update_item.stock = item.stock

    db.commit()

    return update_item

@app.delete('/item/delete/{item_id}', status_code = status.HTTP_200_OK)
def deleteItem(item_id: str):
    item_id = int(item_id)
    check_item = db.query(models.Item).filter(models.Item.item_id == item_id).first()

    if check_item is None:
        raise HTTPException(status_code = 404, detail = "Item's not found")

    db.delete(check_item)
    db.commit()

    return check_item

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=20774)

