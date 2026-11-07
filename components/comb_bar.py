import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))


from dash import html
import dash_bootstrap_components as dbc

from components.metric_card import metric_card
from analytics.donations import kpi_card
from analytics.donors import donor_kpi_card
from analytics.campaigns import campaigns_kpi_bar

def make_kpi_bar():
	total_revenue, revenue_usa, total_donors = kpi_card()
	bar = dbc.Row([
		dbc.Col(metric_card(
			card_id="total-revenue",
			title="Total Revenue",
			value=f"$ {total_revenue:,}",
		)),
		dbc.Col(metric_card(
			card_id="revenue-USA",
			title="Revenue from USA",
			value=f"$ {revenue_usa:,.2f}",
		)),
		dbc.Col(metric_card(
			card_id="revenue-others",
			title="Revenue from Others",
			value=f"$ {total_donors:,.2f}",
		))

	])
	return bar

def make_donors_kpi_bar(start_date, end_date):
	total_donors, avg_lifetime_donation, new_donors = donor_kpi_card(start_date, end_date)
	bar = dbc.Row([
		dbc.Col(metric_card(
			card_id="total-donors",
			title="Total Donors",
			value=f"{total_donors:,}",
		)),
		dbc.Col(metric_card(
			card_id="avg-lifetime-donation",
			title="Average Lifetime Donation",
			value=f"$ {avg_lifetime_donation:,.2f}",
		)),
		dbc.Col(metric_card(
			card_id="new-donors",
			title="New Donors",
			value=f"{new_donors:,.2f}",
		))

	])
	return bar

def make_campaigns_kpi_bar():
	total_campaigns, successful_campaigns, total_raised_usd, avg_achievement_pt, avg_campaign_duration = campaigns_kpi_bar()
	bar = dbc.Row([
		dbc.Col(metric_card(
			card_id="total-campaigns",
			title="Total Campaigns",
			value=f"{total_campaigns:,}",
		)),
		dbc.Col(metric_card(
			card_id="successful-campaigns",
			title="Successful Campaigns",
			value=f"{successful_campaigns}",
		)),
		dbc.Col(metric_card(
			card_id="total-raised-usd",
			title="Total Raised",
			value=f"$ {total_raised_usd:,.2f}",
		)),
		dbc.Col(metric_card(
			card_id="avg-achievement-pt",
			title="Avg Achievement Percentage",
			value=f"{avg_achievement_pt:,.2f}%",
		)),
		dbc.Col(metric_card(
			card_id="avg-campaign-duration",
			title="Avg Campaign Duration",
			value=f"{avg_campaign_duration:,.2f} days",
		))

	])
	return bar