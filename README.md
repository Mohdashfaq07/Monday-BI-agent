#  Monday BI Agent

An AI-powered Business Intelligence (BI) assistant that connects to monday.com boards, normalizes data, and generates actionable insights such as revenue summaries and sector-wise analytics.

---

##  Live Prototype

**Live URL:** web-production-79021.up.railway.app

The application is fully hosted and requires no local setup for basic testing.

---

##  Problem Statement

Business teams using monday.com often struggle to quickly extract meaningful insights from raw board data. Manual analysis is time-consuming and error-prone.

**Solution:** Monday BI Agent automates data extraction, normalization, and insight generation through an intelligent pipeline.

---

##  Key Features

*  Connects to monday.com API
*  Data normalization pipeline
*  Revenue summary generation
*  Sector-wise analytics
*  FastAPI-powered backend
*  Cloud deployed (production ready)

---

##  Tech Stack

**Backend**

* FastAPI
* Python
* Uvicorn

**Data & Integration**

* monday.com GraphQL API
* Custom BI Engine

**Deployment**

* Railway (free tier)

---

##  Project Structure

```
Monday-BI-agent/
│
├── app.py                # FastAPI entry point
├── bi_engine.py          # Business logic & analytics
├── data_normalizer.py    # Data cleaning utilities
├── llm_engine.py         # LLM insight generation
├── monday_client.py      # monday.com API client
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment config
└── README.md             # Project documentation
```

---

##  API Endpoints

### Health Check

```
GET /
```

**Response**

```json
{ "status": "running" }
```

---

### Revenue Summary

```
POST /revenue-summary
```

Generates revenue insights from monday board data.

---

### Pipeline by Sector

```
POST /pipeline-by-sector
```

Returns sector-wise pipeline analytics.

---

##  Local Setup (Optional)

If you want to run locally:

```bash
# 1. Clone repo
git clone https://github.com/Mohdashfaq07/Monday-BI-agent.git
cd Monday-BI-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Environment Variables

Create a `.env` file:

```
MONDAY_API_KEY=eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYyNzEwNzE4NywiYWFpIjoxMSwidWlkIjoxMDA0MDIxOTEsImlhZCI6IjIwMjYtMDItMjhUMDg6MDU6MjcuMDAwWiIsInBlciI6Im1lOndyaXRlIiwiYWN0aWQiOjMzOTk3NDI3LCJyZ24iOiJhcHNlMiJ9.kfPmuZCliSLiW6RSni2i44Sou2C-wfwWomA8vwxM2To
```
**Never commit your real API key.**

---

##  Testing the API

Use Swagger UI:

```
https://web-production-79021.up.railway.app/docs
```

Or via curl:

```bash
curl https://web-production-79021.up.railway.app/
```

---

##  Decision Log (Summary)

* Chose FastAPI for lightweight high-performance APIs
* Modular BI engine for scalability
* Normalization layer to handle inconsistent monday data
* Cloud deployment for zero-setup evaluation

*(Full decision log provided separately as PDF.)*

---

## Future Improvements

* Authentication layer
* Caching for faster analytics
* More advanced BI visualizations
* Multi-board aggregation
* Frontend dashboard

---

## Author

**Mohammed Ashfaq M**

---

##  License

This project is submitted for evaluation purposes.

---

⭐ If you found this project useful, consider giving it a star!
