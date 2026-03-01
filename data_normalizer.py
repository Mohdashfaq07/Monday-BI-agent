import pandas as pd

def normalize_items(raw_items):
    rows = []

    for item in raw_items:
        row = {"name": item.get("name")}

        for col in item.get("column_values", []):
            key = col["column"]["title"]
            value = col.get("text")

            if value in ("", None, "null"):
                value = None

            row[key] = value

        rows.append(row)

    df = pd.DataFrame(rows)

    df = df.replace({"": None, "N/A": None})

    return df
