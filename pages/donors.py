import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/donors", name="donors", order=2)

from components.input_comps import date_input, dropdown_input
from analytics.donors import donor_kpi_card
from components.metric_card import metric_card

layout = html.Div([
	html.H2("Donors Overview", className="page-title"),
	html.Div(id="donor-kpi-bar", className="card-container"),
	html.Div(className="page-inputs",
	         children=[
				date_input("filter-start-date", "Start Date:", default_date="2024-11-05"),
				date_input("filter-end-date", "End Date:", default_date="2025-11-06"),
			 ]),
	html.Div(className="donor-first-row", children=[
	dcc.Graph(id="donor-growth-line", className="big-figure-container"),
	dcc.Graph(id="donor-channel-pie", className="small-figure-container")
	]),
	html.Div(className="donor-second-row", children=[
	dcc.Graph(id="donor-type-pie", className="small-figure-container"),
	dcc.Graph(id="donor-country-bar", className="big-figure-container"),
	])

], className="page-container")