from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from models.wallet import Wallet, Currency

from schemas.wallet_schemas import Response, CreateRequestWallet, CreateRequestCurrency
# from models import Body
from config.database import Base, engine, get_db
from pydantic import BaseModel

# Wallet.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def home():
    # external_wallet = {
    #     'currency': 'rub',
    #     'amount': 156.10
    # }
    
    # wallet = Wallet(**external_wallet)

    return {}


@app.post("/currencies")
async def currencies(currency: CreateRequestCurrency, db: Session = Depends(get_db)):
    rec = Currency(**currency.dict())
     
    db.add(rec)
    db.commit()
    db.refresh(rec)
        
    return Response(
        status=200, 
        message="Ok",
        data=rec
    )

    return {}

@app.get("/wallets")
def wallets(db: Session = Depends(get_db)):
    wallets = db.query(Wallet).all()
    
    return wallets

@app.post("/wallets")
async def wallets(wallet: CreateRequestWallet, db: Session = Depends(get_db)):
    currency = db.query(Currency).get(wallet.currency_id)

    if not currency:
        return Response(
            status=404,
            message="Not found",
            data={}
        )

    w = Wallet(**wallet.dict())
  
    db.add(w)
    db.commit()
    db.refresh(w)
        
    return Response(
        status=200, 
        message="Ok",
        data=w
    )


@app.get("/wallets/{wallet_id}")
def read_item(wallet_id: int, q: Union[str, None] = None):
    # Wallet().find(pk=wallet_id)

    return {"wallet_id": wallet_id, "q": q}
