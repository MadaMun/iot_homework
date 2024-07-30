from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'], description=book['description'], catagory=book['catagory'], short=book['short'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(response: Response ,book_id: int, book: dict, db: Session = Depends(get_db),):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        return response.status_code == 404

@router_v1.delete('/books/{book_id}')
async def delete_book(response: Response, book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        return response.status_code == 404





@router_v1.get('/drinks')
async def get_drinks(db: Session = Depends(get_db)):
    return db.query(models.Drink).all()

@router_v1.get('/drinks/{drink_id}')
async def get_drink(drink_id: int, db: Session = Depends(get_db)):
    return db.query(models.Drink).filter(models.Drink.id == drink_id).first()

@router_v1.post('/drinks')
async def create_drink(drink: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newdrink = models.Drink(menu=drink['menu'], prics=drink['prics'])
    db.add(newdrink)
    db.commit()
    db.refresh(newdrink)
    response.status_code = 201
    return newdrink

@router_v1.patch('/drinks/{drink_id}')
async def update_drink(response: Response ,drink_id: int, drink: dict, db: Session = Depends(get_db),):
    db_drink = db.query(models.Drink).filter(models.Drink.id == drink_id).first()
    if db_drink:
        for key, value in drink.items():
            setattr(db_drink, key, value)
        db.commit()
        db.refresh(db_drink)
        return db_drink
    else:
        return response.status_code == 404

@router_v1.delete('/drinks/{drink_id}')
async def delete_drink(response: Response, drink_id: int, db: Session = Depends(get_db)):
    db_drink = db.query(models.Drink).filter(models.Drink.id == drink_id).first()
    if db_drink:
        db.delete(db_drink)
        db.commit()
        return {"message": "drink deleted successfully"}
    else:
        return response.status_code == 404





@router_v1.get('/orders')
async def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/orders/{order_id}')
async def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

@router_v1.post('/orders')
async def create_order(order: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    neworder = models.Order(id=order['id'], menu=order['menu'], much=order['much'], note=order['note'])
    db.add(neworder)
    db.commit()
    db.refresh(neworder)
    response.status_code = 201
    return neworder

@router_v1.patch('/orders/{order_id}')
async def update_order(response: Response ,order_id: int, order: dict, db: Session = Depends(get_db),):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        for key, value in order.items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        return response.status_code == 404

@router_v1.delete('/orders/{order_id}')
async def delete_order(response: Response, order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return {"message": "order deleted successfully"}
    else:
        return response.status_code == 404

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
