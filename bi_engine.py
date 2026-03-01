import pandas as pd

def pipeline_by_sector(deals_df):
    """
    Computes total pipeline value grouped by sector.
    Works with messy Monday exports.
    """

    deals_df.columns = deals_df.columns.str.strip().str.lower()
    print("DEBUG COLUMNS:", deals_df.columns.tolist())

    sector_col = None
    possible_sector_cols = [
        "sector",
        "sector/service",
        "industry",
        "vertical"
    ]

    for col in possible_sector_cols:
        if col in deals_df.columns:
            sector_col = col
            break

    if sector_col is None:
        return {"warning": "Sector column missing"}

    value_col = None
    possible_value_cols = [
        "value",
        "deal value",
        "amount",
        "deal amount"
    ]

    for col in possible_value_cols:
        if col in deals_df.columns:
            value_col = col
            break

    if value_col is None:
        return {"warning": "Value column missing"}

    deals_df[value_col] = (
        deals_df[value_col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.extract(r"(\d+\.?\d*)")[0]
    )

    deals_df[value_col] = pd.to_numeric(
        deals_df[value_col],
        errors="coerce"
    ).fillna(0)

    deals_df = deals_df[deals_df[sector_col].notna()]
    deals_df = deals_df[deals_df[sector_col] != ""]
    deals_df = deals_df[deals_df[sector_col] != "sector/service"]
    result = (
        deals_df
        .groupby(sector_col)[value_col]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    return result

def revenue_summary(df):
    """
    Basic revenue summary.
    Safe fallback implementation.
    """

    df.columns = df.columns.str.strip().str.lower()

    possible_value_cols = [
        "value",
        "deal value",
        "amount",
        "deal amount"
    ]

    value_col = None
    for col in possible_value_cols:
        if col in df.columns:
            value_col = col
            break

    if value_col is None:
        return {"warning": "Value column missing"}

    df[value_col] = (
        df[value_col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.extract(r"(\d+\.?\d*)")[0]
    )

    df[value_col] = pd.to_numeric(
        df[value_col],
        errors="coerce"
    ).fillna(0)

    return {
        "total_revenue": float(df[value_col].sum()),
        "avg_revenue": float(df[value_col].mean()),
        "deal_count": int(len(df))
    }