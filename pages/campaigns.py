import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/campaigns", name="campaigns", order=3)

from components.comb_bar import make_campaigns_kpi_bar
from analytics.campaigns import (campaigns_performance_bar, by_category_count, 
                                 by_category_amount, make_grid
                                 )

layout = html.Div([
	html.H2("Campaigns Overview", className="page-title"),
	html.Div(make_campaigns_kpi_bar(), className="card-container"),
	html.Div(className="campaigns-first-row", 
	         children=[
				dcc.Graph(id="campaign-performance", className="big-figure-container-2", figure=campaigns_performance_bar()),
				dcc.Graph(id="campaign-category-type", className="small-figure-container", figure=by_category_count()),
				dcc.Graph(id="campaign-contribution", className="small-figure-container-2", figure=by_category_amount()),
			]),
	html.Div(className="campaigns-second-row", 
				children=[
				html.Div(make_grid("ag-theme-alpine"))
			])
], className="page-container")