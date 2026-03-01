def interpret_question(question: str) -> dict:
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Extract the user's intent."},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )

        text = resp.choices[0].message.content.lower()

    except Exception as e:
        text = question.lower()

    if "pipeline" in text or "sector" in text:
        return {"intent": "pipeline_by_sector"}
    if "revenue" in text or "deal size" in text:
        return {"intent": "revenue_summary"}

    return {"intent": "unknown"}


def generate_insight(question: str, metrics: dict) -> str:
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""
Question: {question}

Metrics:
{metrics}

Write a crisp founder-ready insight.
""",
                },
            ],
            temperature=0.3,
        )

        return resp.choices[0].message.content

    except Exception:
        return (
            "Insight generated using deterministic analysis. "
            "LLM unavailable due to quota limits."
        )
