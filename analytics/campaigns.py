import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import dash_ag_grid as dag

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

campaigns = pd.read_csv(DATA_DIR / "campaigns.csv")

def campaigns_kpi_bar():
	total_campaigns = campaigns["campaign_id"].nunique()
	total_raised_usd = campaigns["actual_raised_usd"].sum()
	avg_achievement_pt = campaigns["achievement_percentage"].mean()
	successful_campaigns = len(campaigns[campaigns["achievement_percentage"] >= 100.00 ])

	campaigns["start_date"] = pd.to_datetime(campaigns["start_date"])
	campaigns["end_date"] = pd.to_datetime(campaigns["end_date"])
	campaigns["duration"] = campaigns["end_date"] - campaigns["start_date"]
	campaigns["duration_days"] = campaigns["duration"].dt.days
	avg_campaign_duration = campaigns["duration_days"].mean()
	return total_campaigns, successful_campaigns, total_raised_usd, avg_achievement_pt, avg_campaign_duration

def campaigns_performance_bar():
	goal = [100] * len(campaigns)
	fig = go.Figure()
	fig.add_trace(go.Bar(
		x=campaigns["campaign_id"],
		y=goal,
		name="Goal Target",
		marker_color="rgba(255, 255, 255, 0.2)",
	))
	fig.add_trace(go.Bar(
		x=campaigns["campaign_id"],
		y=campaigns["achievement_percentage"],
		name="Actual Achieved",
		marker_color="#1E88E5",
	))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Campaign Performance",
		xaxis_title="Campaign",
		yaxis_title="Performance",
		barmode="overlay",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	fig.update_yaxes(
		range=[0, 140]
	)
	fig.update_xaxes(
		tickmode="linear",
		tick0=0,
		dtick=1,
	)
	return fig

def by_category_count():
	by_category = campaigns.groupby("category")["campaign_id"].nunique().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Pie(labels=list(by_category["category"].values), values=by_category["campaign_id"].values, hole=0.6))
	fig.update_layout(
		margin=dict(l=70, r=30, t=70, b=0),
		title="Campaigns by Category",
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
	)
	return fig

def by_category_amount():
	by_category_amount = campaigns.groupby("category")["actual_raised_usd"].sum().reset_index()
	fig = go.Figure()
	fig.add_trace(go.Bar(
		x=by_category_amount["actual_raised_usd"],
		y=by_category_amount["category"],
		orientation="h",
		name="Campaigns"
	))
	fig.update_layout(
		margin=dict(l=90, r=30, t=70, b=0),
		title="Campaign Contribution",
		xaxis_title="Amount (USD)",
		yaxis=dict(ticklabelstandoff=15),
		paper_bgcolor="rgba(0, 0, 0, 0)",
		plot_bgcolor="rgba(0, 0, 0, 0)",
		font_color="white",
		font=dict(family="arial"),
		width=100,
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

def make_grid(className):
	grid = dag.AgGrid(
		id="campaign-ag-grid",
		rowData=campaigns.to_dict("records"),
		columnDefs=[{"field": i} for i in campaigns.columns],
		defaultColDef={"sortable": True, "filter": True, "resizable": True},
		dashGridOptions={"pagination": True},
		className=className
	)
	return grid
