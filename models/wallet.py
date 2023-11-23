# from pydantic import BaseModel
from config.database import Base


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    currency = relationship('Currency')


class Currency(Base):
    __tablename__ = 'currencies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # wallets = relationship("Wallet", back_populates="wallets")

