# from pydantic import BaseModel
from config.database import Base


from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.orm import relationship


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    amount = Column(Float)