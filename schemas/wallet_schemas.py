from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CreateRequestCurrency(BaseModel):
    name: str


class CreateRequestWallet(BaseModel):
    currency_id: Optional[int | None] = None
    amount: Optional[float| None] = None


class Response(GenericModel, Generic[T]):
    data: Optional[T]
    message: str = 'Success'
    code: int = 200