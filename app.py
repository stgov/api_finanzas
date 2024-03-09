import yfinance as yf
from fastapi import FastAPI

app = FastAPI()

@app.get("/{stock}")
async def main(stock: str):
    stock = yf.Ticker(stock)
    data = stock.history(period="1d")
    return data["Close"].iloc[-1]