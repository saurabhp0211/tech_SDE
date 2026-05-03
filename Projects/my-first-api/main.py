from fastapi import FastAPI,Depends,HTTPException
from schemas import ExpenseCreate, ExpenseResponse,ExpenseUpdate
from sqlalchemy.orm import Session
import models
from database import engine, get_db



models.Base.metadata.create_all(bind=engine)


app=FastAPI(title="Saurabh's Expense Tracker")


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Expense Tracker API",
        "version":"1.0.0"
    }

@app.get("/expenses",response_model=list[ExpenseResponse])
def get_expenses(db: Session=Depends(get_db)):
    expenses=db.query(models.Expense).all()
    return expenses

@app.post("/expenses", response_model=ExpenseResponse)
def create_expense(expense:ExpenseCreate,db:Session=Depends(get_db)):

    new_expense=models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        expense_date=expense.expense_date
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.patch("/expenses/{expense_id}",response_model=ExpenseResponse)
def update_expense(expense_id:int,updated_data:ExpenseUpdate,db:Session=Depends(get_db)):
    db_expense=db.query(models.Expense).filter(models.Expense.id==expense_id).first()

    if not db_expense:
        raise HTTPException(status_code=404,detail="Expense not found")
    
    update_dict=updated_data.model_dump(exclude_unset=True)

    for key,value in update_dict.items():
        setattr(db_expense,key,value)
    
    db.commit()
    db.refresh(db_expense)

    return db_expense




                                  