from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models.wallet import Wallet

from schemas.wallet_schemas import Response, CreateRequestWallet
# from models import Body
from config.database import engine, get_db
from pydantic import BaseModel

Wallet.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def home():
    external_wallet = {
        'currency': 'rub',
        'amount': 156.10
    }
    
    wallet = Wallet(**external_wallet)

    return wallet


@app.get("/wallets")
def wallets(q: Union[str, None] = None):
    return {"q": q}


@app.post("/wallets")
async def wallets(wallet: CreateRequestWallet, db: Session = Depends(get_db)):
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
