import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from dash import Dash, html, dcc, Input, Output, State, ctx, no_update
from dash.exceptions import PreventUpdate

from analytics.donations import (make_total_donations_graph, 
									kpi_card, payment_method_pie, donation_type_pie,
									country_bar
									)
from components.comb_bar import make_donors_kpi_bar
from analytics.donors import donors_over_time, by_channel_pie, by_type, donors_by_country


def register_app_callbacks(app):
	@app.callback(
		Output("total-donations-fig", "figure"),
		Output("payment-method-pie", "figure"),
		Output("donation-type-pie", "figure"),
		Output("country-amount-bar", "figure"),
		Input("filter-start-date", "date"),
		Input("filter-end-date", "date")
	)
	def update_graph(start_date, end_date):
		donations_graph = make_total_donations_graph(start_date, end_date)
		payment_pie = payment_method_pie(start_date, end_date)
		type_pie = donation_type_pie(start_date, end_date)
		country_bar_fig = country_bar(start_date, end_date)
		return donations_graph, payment_pie, type_pie, country_bar_fig

	@app.callback(
		Output("donor-kpi-bar", "children"),
		Output("donor-growth-line", "figure"),
		Output("donor-channel-pie", 'figure'),
		Output("donor-type-pie", "figure"),
		Output("donor-country-bar", "figure"),
		Input("filter-start-date", "date"),
		Input("filter-end-date", "date")
	)
	def update_donor_kpi_bar(start_date, end_date):
		kpi_bar = make_donors_kpi_bar(start_date, end_date)
		donor_growth_line = donors_over_time(start_date, end_date)
		donor_channel_pie = by_channel_pie(start_date, end_date)
		donor_type_pie = by_type(start_date, end_date)
		donor_country_bar = donors_by_country(start_date, end_date)
		return kpi_bar, donor_growth_line, donor_channel_pie, donor_type_pie, donor_country_bar


