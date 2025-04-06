from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base, TOKENSINFO, PORTFOLIO
from .schemas import TokenInfoCreate, TokenInfo, PortfolioCreate, Portfolio  
from datetime import date
from pydantic import ValidationError
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    #allow_origin_regex=r'https?://(?:127\.0\.0\.1|localhost):300[0-9]',
    allow_origins=["*"],
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def hello():
    return "Hello from FastAPI"


@app.post("/tokens/", response_model=TokenInfoCreate)
def create_token(token: TokenInfoCreate, db: Session = Depends(get_db)):

    db_token = db.query(TOKENSINFO).filter(TOKENSINFO.ticker == token.ticker).first()
    if db_token:
        raise HTTPException(status_code=400, detail="Ticker already exists")
    
    db_token = TOKENSINFO(
        ticker=token.ticker,
        information=token.information
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


@app.post("/portfolio/", response_model=PortfolioCreate)
def create_portfolio_entry(entry: PortfolioCreate, db: Session = Depends(get_db)):
    try:
        token = db.query(TOKENSINFO).filter(TOKENSINFO.ticker == entry.ticker).first()
        if not token:
            raise HTTPException(status_code=404, detail="Token not found")
        
        if entry.sell_date and entry.sell_date < entry.buy_date:
            raise HTTPException(status_code=400, detail="Sell date must be after buy date")
        
        db_entry = PORTFOLIO(
            ticker=entry.ticker,
            amount=entry.amount,
            buy_date=entry.buy_date,
            sell_date=entry.sell_date,
            buy_price=entry.buy_price,
            sell_price=entry.sell_price
        )
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
        return db_entry
        
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@app.get("/tokens/", response_model=list[TokenInfo])
def get_tokens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tokens = db.query(TOKENSINFO).offset(skip).limit(limit).all()
    return tokens


@app.get("/portfolio/", response_model=list[Portfolio])
def get_portfolio_entries(
    ticker: str | None = None,
    active_only: bool = False,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(PORTFOLIO)
    

    if ticker:
        query = query.filter(PORTFOLIO.ticker == ticker)
    

    if active_only:
        query = query.filter(PORTFOLIO.sell_date.is_(None))
    
    entries = query.offset(skip).limit(limit).all()
    return entries


@app.get("/portfolio/{entry_id}", response_model=Portfolio)
def get_portfolio_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(PORTFOLIO).filter(PORTFOLIO.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Portfolio entry not found")
    return entry