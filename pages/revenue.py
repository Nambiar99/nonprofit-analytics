import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.input_comps import date_input, dropdown_input
from components.comb_bar import make_kpi_bar
from components.metric_card import metric_card

dash.register_page(__name__, path="/", name="revenue", order=1)

cities = ["New York", "London", "Paris", "Tokyo", "Mumbai"]
metrics = ["Revenue", "Profit", "Users", "Retention"]

layout = html.Div([
	html.H2("Revenue Overview", className="page-title"),
	html.Div(make_kpi_bar(), className="card-container"),
	html.Div(
	className="page-inputs",
	children=[
	date_input("filter-start-date", "Start Date:", default_date="2024-11-05"),
	date_input("filter-end-date", "End Date:", default_date="2025-11-06"),
			]
			),
	html.Div(children=[
		dcc.Graph(id="total-donations-fig", className="big-figure-container"),
		dcc.Graph(id="payment-method-pie", className="small-figure-container"),
	], className="revenue-first-row"),
	html.Div(children=[
	dcc.Graph(id="donation-type-pie", className="small-figure-container"),
	dcc.Graph(id="country-amount-bar", className="big-figure-container")
	], className="revenue-second-row")
], className="page-container"
)


