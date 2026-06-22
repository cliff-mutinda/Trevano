from flask import Flask, render_template, jsonify, request
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)

API_URL = os.getenv("TRADING_API") 

def fetch_data():
    """Fetch securities data from the configured API."""
    if not API_URL:
        return None, "API URL is not configured. Please set API_URL in app.py."
    try:
        response = requests.post(API_URL, headers={"Content-Type": "application/json"}, timeout=100)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Could not connect to the API. Check the URL and your network."
    except requests.exceptions.Timeout:
        return None, "API request timed out."
    except requests.exceptions.HTTPError as e:
        return None, f"HTTP error: {e}"
    except Exception as e:
        return None, f"Unexpected error: {e}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/securities")
def api_securities():
    """Proxy endpoint — returns raw JSON from the upstream API."""
    data, error = fetch_data()
    if error:
        return jsonify({"error": error}), 503
    return jsonify(data)


@app.route("/api/summary")
def api_summary():
    """Returns high-level counts / stats."""
    data, error = fetch_data()
    if error:
        return jsonify({"error": error}), 503

    segments   = {}
    instruments = {}
    intraday_count = 0

    for item in data:
        seg = item.get("Segment", "Unknown")
        ins = item.get("InstrumentType", "Unknown")
        segments[seg]    = segments.get(seg, 0) + 1
        instruments[ins] = instruments.get(ins, 0) + 1
        if item.get("AllowIntradayTrading"):
            intraday_count += 1

    return jsonify({
        "total": len(data),
        "intraday_enabled": intraday_count,
        "segments": segments,
        "instrument_types": instruments,
    })


@app.route("/equity")
def equity():
    return render_template("equity.html")


@app.route("/derivatives")
def derivatives():
    return render_template("derivatives.html")


@app.route("/debt")
def debt():
    return render_template("debt.html")


@app.route("/search")
def search():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
