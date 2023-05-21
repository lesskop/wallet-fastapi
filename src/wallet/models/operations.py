from datetime import date
from typing import Optional
from enum import Enum
from pydantic import BaseModel, condecimal


class OperationKind(str, Enum):
    INCOME = 'income'
    EXPENSE = 'expense'


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: condecimal(max_digits=10, decimal_places=2)
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase):
    pass
