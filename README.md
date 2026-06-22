# Trevano 📈 — NSE Market Viewer

Trevano is a modern, responsive, and lightweight web dashboard for viewing and searching securities listed on the Nairobi Securities Exchange (NSE). The application serves as a clean client interface for real-time market data, fetching and structuring information from an upstream Trading API.

🔗 **Live Version:** [trevano.cliffmutinda.com](https://trevano.cliffmutinda.com)

---

## 🌟 Features

- **📊 Comprehensive Dashboard:**
  - High-level overview card stats (Total Securities, Intraday Enabled count, Equity count, Debt instruments count).
  - Dynamic segment breakdown bar charts showing the distribution of securities.
  - Recent activity snapshot listing the latest trading instruments.

- **💼 Segment-Specific Views:**
  - **Equity:** Browse listed companies with interactive sorting (Symbol, Name, LTP, Close, Change %) and fast filtering (search/intraday eligibility).
  - **Derivatives:** Track options and futures contracts.
  - **Debt:** Monitor bond markets and fixed-income instruments.

- **🔍 Advanced Search:**
  - Instant, client-side querying across all market segments (Equity, Derivatives, Debt, OTC).
  - Multi-criteria filtering by symbol, company name, or security code.
  - Click-to-view detailed drawer displaying comprehensive trading metrics (limits, tick size, lot sizes).

- **🟢 Real-Time API Health Status:**
  - Header status bar checks connection health and security counts from the upstream API automatically.

- **📱 Sleek, Responsive UI:**
  - Clean styling with modern typography, smooth transitions, CSS variables, and a mobile-friendly hamburger navigation menu.

---

## 🏗️ Tech Stack

- **Backend:** Python, [Flask](https://flask.palletsprojects.com/)
- **Frontend:** Vanilla HTML5, Modern CSS (Glassmorphism, custom scrollbars, and flexbox grid layouts), Vanilla JavaScript (ES6, Fetch API)
- **Data Integration:** Requests (syncing with external REST API)
- **Environment Management:** `python-dotenv`

---

## 🔌 API Integration Details

Trevano acts as a middleman/proxy between the client browser and a secure backend Trading API. To run correctly, it expects the upstream API (configured via `TRADING_API`) to return a JSON array of securities with the following properties:

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `Symbol` | String | Trading ticker symbol (e.g. `SCOM`, `EQTY`) |
| `SecurityName` | String | Full name of the listing (e.g. `Safaricom PLC`) |
| `Segment` | String | Market segment (`Equity`, `Derivatives`, `Debt`, `OTC`) |
| `InstrumentType` | String | Type of instrument (e.g. `Ordinary Shares`) |
| `LTP` | Float | Last Traded Price |
| `ClosingPrice` | Float | Previous day's closing price |
| `AllowIntradayTrading`| Boolean| Intraday trading eligibility flag |
| `SecurityCode` | String | Unique identifier code |
| `BuyLowerLimit` | Float | Lowest allowed bidding price |
| `BuyUpperLimit` | Float | Highest allowed bidding price |
| `TickSize` | Float | Minimum price movement unit |
| `MarketLot` | Integer| Minimum trading unit size |

---

## 🛠️ Setup & Installation Instructions

Follow these instructions to set up and run Trevano locally.

### Prerequisites
Make sure you have the following installed on your machine:
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (optional, for cloning)

### 1. Clone the Repository
Clone the project to your local machine:
```bash
git clone https://github.com/your-username/trevano.git
cd trevano
```
*(If you are setting this up manually, navigate into the directory where you extracted the project files)*

### 2. Set Up a Virtual Environment
It is highly recommended to run the application in a virtual environment to manage dependencies:

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install all the required python modules listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the template environment file:
```bash
cp .env.example .env
```
Open `.env` in your text editor and specify your upstream API endpoint:
```env
TRADING_API=https://your-upstream-trading-api-endpoint.com/securities
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
By default, the server runs in debug mode at:  
🔗 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📁 Project Structure

```text
trevano/
│
├── static/
│   ├── css/
│   │   └── style.css       # Core stylesheets & variables
│   └── js/
│       └── main.js        # Mobile menu toggle & API status polling
│
├── templates/
│   ├── base.html          # Global layout structure
│   ├── index.html         # Dashboard & segment statistics
│   ├── equity.html        # Equities list & sorting interface
│   ├── derivatives.html   # Derivatives viewer
│   ├── debt.html          # Fixed income list
│   └── search.html        # Global search and detailed metrics
│
├── .env.example           # Reference configuration variables
├── app.py                 # Flask server routes and proxy endpoints
└── requirements.txt       # Project dependencies
```
