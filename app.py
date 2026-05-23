from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Gold AI Signal server is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    symbol = data.get("symbol", "XAUUSD")
    action = data.get("action", "ALERT")
    price = data.get("price", "N/A")
    timeframe = data.get("timeframe", "N/A")
    note = data.get("note", "TradingView alert received")

    message = f"""
🚨 Gold Signal Alert

Symbol: {symbol}
Action: {action}
Price: {price}
Timeframe: {timeframe}

Note: {note}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})

    return {"status": "sent"}
