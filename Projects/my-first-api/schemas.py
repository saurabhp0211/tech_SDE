from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


# the base schema where we define what exactly goes inside the expense record we are updating
class ExpenseBase(BaseModel):
    title: str=Field(..., min_length=3, max_length=50, example="Starbucks Coffee")
    amount: float= Field(..., gt=0, example=250.75)
    category: str= Field(..., example="Food")
    expense_date: Optional[date]= Field(default_factory=date.today)


# input from the user
class ExpenseCreate(ExpenseBase):
    pass 

# Schema for reading an expense
class ExpenseResponse(ExpenseBase):
    id:int

    class Config:
        from_attributes= True

class ExpenseUpdate(BaseModel):
    title: Optional[str]=None
    amount: Optional[float]=None
    category:Optional[str]=None
    expense_date: Optional[date]=None





