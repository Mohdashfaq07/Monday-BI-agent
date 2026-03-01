from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI

from monday_client import fetch_board_items
from data_normalizer import normalize_items
from bi_engine import pipeline_by_sector, revenue_summary
from llm_engine import interpret_question, generate_insight


app = FastAPI(
    title="Monday BI Agent",
    description="Founder-level business intelligence over monday.com",
    version="1.0.0",
)

DEALS_BOARD_ID = int(os.getenv("DEALS_BOARD_ID"))
WORK_BOARD_ID = int(os.getenv("WORK_BOARD_ID"))


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/ask")
def ask_agent(question: str):
    trace = []

    # Step 1 — intent understanding
    trace.append("LLM interpreting question...")
    intent_data = interpret_question(question)
    intent = intent_data["intent"]

    # Step 2 — LIVE monday call
    trace.append("Fetching Deals board (live)...")
    deals_raw = fetch_board_items(DEALS_BOARD_ID)
    deals_items = deals_raw["data"]["boards"][0]["items_page"]["items"]
    deals_df = normalize_items(deals_items)

    # Step 3 — compute metrics
    trace.append(f"Computing metric: {intent}")

    if intent == "pipeline_by_sector":
        metrics = pipeline_by_sector(deals_df)
    elif intent == "revenue_summary":
        metrics = revenue_summary(deals_df)
    else:
        metrics = {"note": "Intent unclear"}

    # Step 4 — generate insight
    trace.append("LLM generating insight...")
    insight = generate_insight(question, metrics)

    return {
        "question": question,
        "intent": intent,
        "metrics": metrics,
        "insight": insight,
        "trace": trace,
        "data_quality_note": "Nulls and inconsistent values normalized.",
    }
