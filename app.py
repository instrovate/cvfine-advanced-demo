import pandas as pd
import streamlit as st

from anomaly import flag_anomalies

st.set_page_config(page_title="Weekly Sales Anomaly Check", layout="wide")
st.title("Weekly store sales anomaly check")
st.write("Upload a CSV with columns **store, week, sales_inr**. Each store is compared with its own recent average.")

threshold = st.slider("Flag stores that move more than (%)", 5, 50, 15)
history = st.slider("Weeks of history to average", 2, 12, 4)
file = st.file_uploader("Weekly sales CSV", type="csv")
df = pd.read_csv(file) if file else pd.read_csv("sample_weekly_store_sales.csv")
if not file:
    st.caption("Showing the sample file. Upload your own to replace it.")

result = flag_anomalies(df, threshold, history)
flagged = result[result["flag"] == "Investigate"]
st.metric("Stores to investigate", f"{len(flagged)} of {len(result)}")
st.dataframe(result.style.apply(lambda r: ["background-color: #fde2e1" if r.flag == "Investigate" else "" for _ in r], axis=1),
             width="stretch")
st.bar_chart(result.set_index("store")["deviation_pct"])
st.download_button("Download flagged stores (CSV)", flagged.to_csv(index=False), "flagged_stores.csv")
