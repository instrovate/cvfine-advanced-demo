"""Weekly store sales anomaly check: compare each store with its own recent average."""
import pandas as pd


def flag_anomalies(df: pd.DataFrame, threshold_pct: float = 15.0, history_weeks: int = 4) -> pd.DataFrame:
    """Expects columns store, week, sales_inr. Returns one row per store for the latest week."""
    df = df.copy()
    df["week"] = pd.to_datetime(df["week"])
    last = df["week"].max()
    hist = df[df["week"] < last].sort_values("week").groupby("store").tail(history_weeks)
    avg = hist.groupby("store")["sales_inr"].mean().rename("avg_recent")
    cur = df[df["week"] == last].set_index("store")["sales_inr"].rename("this_week")
    out = pd.concat([avg, cur], axis=1).dropna()
    out["deviation_pct"] = ((out["this_week"] - out["avg_recent"]) / out["avg_recent"] * 100).round(1)
    out["flag"] = out["deviation_pct"].abs().gt(threshold_pct).map({True: "Investigate", False: "OK"})
    return out.sort_values("deviation_pct").reset_index()
