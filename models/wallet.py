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
    code = Column(String)
    # wallets = relationship("Wallet", back_populates="wallets")



class ExchangeTransaction(Base):
    __tablename__ = "exchange_transactions"
    id = Column(Integer, primary_key=True, index=True)

    source = Column(Integer, ForeignKey("wallets.id"))
    target = Column(Integer, ForeignKey("wallets.id"))
    amount = Column(Float)
    rate = Column(Float)