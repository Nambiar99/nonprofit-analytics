import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

donors = pd.read_csv(DATA_DIR / "donors.csv")

def donor_kpi_card(start_date, end_date):
	filtered_df = donors[donors["first_donation_date"].between(start_date, end_date)]
	new_donors = filtered_df["donor_id"].nunique()
	total_donors = donors["donor_id"].nunique()
	average_lifetime_donation = donors["lifetime_donations_usd"].sum() / donors["donor_id"].nunique()
	return total_donors, average_lifetime_donation, new_donors

def donors_over_time(start_date, end_date):
	filtered_df = donors[donors["first_donation_date"].between(start_date, end_date)]
	donor_growth = filtered_df.groupby("registration_date")["donor_id"].nunique().reset_index(name="new_donors")
	donor_growth = donor_growth.sort_values("registration_date").reset_index(drop=True)
	donor_growth["total_donors"] =donor_growth["new_donors"].cumsum()

	fig = go.Figure()
	fig.add_trace(go.Scatter(
		x=donor_growth["registration_date"],
		y=donor_growth["total_donors"],
		mode="lines",
		name="Donors"
	))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donor Growth",
		xaxis_title="Date",
		yaxis_title="Number of Donors",
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

def by_channel_pie(start_date, end_date):
	filtered_df = donors[donors["first_donation_date"].between(start_date, end_date)]
	by_channel = filtered_df.groupby("acquisition_channel")["donor_id"].count().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Pie(
		labels=list(by_channel["acquisition_channel"].values), 
		values=by_channel["donor_id"].values,
		hole=0.6
		))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donor Acquisition Channels",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	return fig

def by_type(start_date, end_date):
	filtered_df = donors[donors["first_donation_date"].between(start_date, end_date)]
	by_type = filtered_df.groupby("donor_type")["donor_id"].count().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Pie(
		labels=list(by_type["donor_type"].values), 
		values=by_type["donor_id"].values,
		hole=0.6
		))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donor Type",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	return fig

def donors_by_country(start_date, end_date):
	filtered_df = donors[donors["first_donation_date"].between(start_date, end_date)]
	by_country = filtered_df.groupby("country")["donor_id"].nunique().reset_index()
	by_country = by_country.sort_values("donor_id", ascending=False)
	fig = go.Figure()
	fig.add_trace(go.Bar(
		x=by_country["country"].values,
		y=by_country["donor_id"].values,
		name="Donors"
	))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Donors by country",
		xaxis_title="Country",
		yaxis_title="Number of Donors",
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
