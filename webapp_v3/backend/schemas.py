from datetime import date
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional

class TokenInfoCreate(BaseModel):
    ticker: str
    information: str

class TokenInfo(TokenInfoCreate):
    id: int
    
    class Config:
        from_attributes = True

class PortfolioCreate(BaseModel):
    ticker: str = Field(..., min_length=3, max_length=24, description="Asset tickers", example="BTC")
    amount: float = Field(..., description="Quantity of units of the asset held")
    buy_date: Optional[date] = Field(None, description="Date when the asset was purchased, in YYYY-MM-DD format.", example="YYYY-MM-DD")
    sell_date: Optional[date] = Field(None, description="Date when the asset was sold, in YYYY-MM-DD format.", example="YYYY-MM-DD")
    buy_price: Optional[float] = Field(None, description="Price per unit of the asset at the time of purchase ")
    sell_price: Optional[float] = Field(None, description="Price per unit of the asset at the time of sale.")

    # @model_validator(mode='after')
    # def validate_buy_or_sell(cls, values):
    #     has_buy = values.buy_date is not None or values.buy_price is not None
    #     has_sell = values.sell_date is not None or values.sell_price is not None

    #     # Rule 1: Reject if both buy AND sell fields are provided
    #     if has_buy and has_sell:
    #         raise ValueError(
    #             "Provide EITHER 'buy_date' + 'buy_price' OR 'sell_date' + 'sell_price', not both."
    #         )

    #     # Rule 2: Buy fields must be complete (both or none)
    #     if (values.buy_date is not None) != (values.buy_price is not None):
    #         raise ValueError(
    #             "Both 'buy_date' and 'buy_price' must be provided together (or neither)."
    #         )

    #     # Rule 3: Sell fields must be complete (both or none)
    #     if (values.sell_date is not None) != (values.sell_price is not None):
    #         raise ValueError(
    #             "Both 'sell_date' and 'sell_price' must be provided together (or neither)."
    #         )

    #     # Rule 4: At least one complete pair must exist
    #     if not (has_buy or has_sell):
    #         raise ValueError(
    #             "Provide either 'buy_date' + 'buy_price' OR 'sell_date' + 'sell_price'."
    #         )

    #     return values

        

class Portfolio(PortfolioCreate):
    id: int = Field(... , description="Unique identifier")
    
    class Config:
        from_attributes = True