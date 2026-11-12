# Weekly Sales Anomaly Check

**Live app:** https://akeskkklcjkkjmqyacpvhb.streamlit.app

A small Streamlit app that tells a retail operations manager which stores need a call this week.
Each store's latest weekly sales are compared with **its own** recent average (not with other stores),
and any store that moves more than the chosen threshold (15% by default) is flagged **Investigate**.

This is the sample project for the **CVFine AI Advanced Sprint** ("Build and ship" milestone):
the analysis from milestones 1 to 3 (Colab notebook, flagged report, AI-written manager summary) turned into a tool
someone else can use.

## How to use it
1. Install: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`
3. Upload a CSV with columns `store, week, sales_inr` (one row per store per week), or use the included
   `sample_weekly_store_sales.csv`. Adjust the threshold and history sliders, then download the flagged stores.

Published free on Streamlit Community Cloud from this repo (no credit card).

## How it works
- `anomaly.py`: `flag_anomalies()` takes the latest week, averages each store's previous N weeks,
  and computes the percentage deviation.
- `app.py`: upload, sliders, colour-coded table, bar chart and CSV download.
- `test_anomaly.py`: checks that the sample flags exactly S04 (-30.9%) and S09 (+35.2%).

Built with help from Claude.ai, which suggested the store-relative comparison and drafted the first version of the code.

## Known limitations
- One threshold for every store: naturally volatile stores will be flagged more often.
  A per-store standard deviation (z-score) would be fairer.
- Planned promotions (Diwali, sales) are flagged like any other spike; there is no promotion column yet.
- A number cannot tell a stock-out from a data error: call the store before acting.

## Feedback from a first user
"This looks great: innovative, and a great learning experience." — Akriti Lal, after trying the live app
