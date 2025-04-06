# backend/models.py
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from .database import Base

class TOKENSINFO(Base):
    __tablename__ = 'TOKENSINFO'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(255), nullable=False, unique=True)
    information = Column(String(255), nullable=False)
    
    
    portfolio_entries = relationship("PORTFOLIO", back_populates="token_info", lazy='joined')

class PORTFOLIO(Base):
    __tablename__ = 'PORTFOLIO'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(255), ForeignKey('TOKENSINFO.ticker'), nullable=False)
    amount = Column(Float, nullable=False)
    buy_date = Column(Date, nullable=True)
    sell_date = Column(Date, nullable=True)
    buy_price = Column(Float, nullable=True)
    sell_price = Column(Float, nullable=True)
    
    token_info = relationship("TOKENSINFO", back_populates="portfolio_entries", lazy='joined')