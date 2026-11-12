import pandas as pd
from anomaly import flag_anomalies


def test_sample_flags_two_stores():
    out = flag_anomalies(pd.read_csv("sample_weekly_store_sales.csv"))
    assert set(out.loc[out.flag == "Investigate", "store"]) == {"S04", "S09"}


def test_threshold_changes_result():
    out = flag_anomalies(pd.read_csv("sample_weekly_store_sales.csv"), threshold_pct=40)
    assert (out.flag == "OK").all()
