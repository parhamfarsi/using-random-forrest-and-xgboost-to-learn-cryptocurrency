# Cryptocurrency 30-Day Modeling — README

## Project overview
This repository implements **supervised** modeling of cryptocurrency price behavior using two approaches:

- **Regression** — predict future price (or return) over the next 30 days.  
- **Classification** — predict a discrete label for the next 30 days (e.g., `UP` / `DOWN` / `STABLE`).  

Both approaches are built using **XGBoost** and **Random Forest** models. These algorithms are chosen for their strong performance on structured/tabular data and their ability to capture nonlinear patterns in cryptocurrency markets.  

Models are trained and evaluated in **30-day windows**. Each approach contains two main scripts (training + evaluation), and there are shared utilities used by both.

---

## Goals
1. Preprocess crypto price and indicator data into 30-day windows.  
2. Train **XGBoost** and **Random Forest** models for regression and classification tasks.  
3. Evaluate performance **per-30-day window** and report metrics (accuracy for classification; RMSE/MAE + direction accuracy for regression).  
4. Save model artefacts, per-window results (CSV), and summary reports.

---

## Repo structure
