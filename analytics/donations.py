import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

donations = pd.read_csv(DATA_DIR / "donations.csv")
donors = pd.read_csv(DATA_DIR / "donors.csv")
total_donations = donations.groupby("donation_date")["amount_usd"].sum().reset_index()

def make_total_donations_graph(start_date, end_date):
	filtered_df = total_donations[total_donations["donation_date"].between(start_date, end_date)]
	fig = go.Figure()
	fig.add_trace(go.Scatter(
		x=filtered_df["donation_date"],
		y=filtered_df["amount_usd"],
		mode="lines+markers",
		name="Donations (USD)"
	))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donations by Date",
		xaxis_title="Date",
		yaxis_title="Amount (USD)",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	fig.update_xaxes(
		showgrid=True,
		gridcolor="rgba(255, 255, 255, 0.2)"
	)
	fig.update_yaxes(
		showgrid=True,
		gridcolor="rgba(255, 255, 255, 0.2)"
	)
	return fig

def payment_method_pie(start_date, end_date):
	filtered_df = donations[donations["donation_date"].between(start_date, end_date)]
	by_payment_method = filtered_df.groupby("payment_method")["amount_usd"].sum().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Pie(
		labels=list(by_payment_method["payment_method"].values), 
		values=by_payment_method["amount_usd"].values,
		hole=0.6
		))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donations by Payment Method",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	return fig

def donation_type_pie(start_date, end_date):
	filtered_df = donations[donations["donation_date"].between(start_date, end_date)]
	by_donation_type = filtered_df.groupby("donation_type")["amount_usd"].sum().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Pie(labels=list(by_donation_type["donation_type"].values), values=by_donation_type["amount_usd"].values, hole=0.6))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donations by Type",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	return fig

def country_bar(start_date, end_date):
	filtered_df = donations[donations["donation_date"].between(start_date, end_date)]
	by_country = filtered_df.groupby("country")["amount_usd"].sum().reset_index()
	by_country = by_country.sort_values(by="amount_usd", ascending=False)
	plot_country = by_country.head(15)
	fig = go.Figure()
	fig.add_trace(go.Bar(
		x=list(by_country["country"].head(10).values),
		y=by_country["amount_usd"].head(10).values
	))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Top 10 Donating Countries",
		xaxis_title="Country",
		yaxis_title="Amount (USD)",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	fig.update_xaxes(
		showgrid=True,
		gridcolor="rgba(255, 255, 255, 0.2)"
	)
	fig.update_yaxes(
		showgrid=True,
		gridcolor="rgba(255, 255, 255, 0.2)"
	)
	return fig

def kpi_card():
	filtered_df = donations.groupby("country")["amount_usd"].sum().reset_index()
	total_revenue = filtered_df["amount_usd"].sum()
	revenue_usa = filtered_df[filtered_df["country"] == "United States"]["amount_usd"].sum()
	revenue_others = filtered_df[~(filtered_df["country"] == "United States")]["amount_usd"].sum()
	return total_revenue, revenue_usa, revenue_others


