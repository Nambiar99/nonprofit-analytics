from dash import html
import dash_bootstrap_components as dbc

def create_title_bar():
	title_bar = html.Div(
		[
			html.H2("Global Donation Dashboard", className="titlebar-title"),
			dbc.Nav(
					[
						dbc.NavLink("Revenue", href="/", active="exact", className="sidebar-options"),
						dbc.NavLink("Donors", href="/donors", active="exact", className="sidebar-options"),
						dbc.NavLink("Campaigns", href="/campaigns", active="exact", className="sidebar-options"),
					], vertical=False, pills=True, className="sidebar-options"
				)
		], className="titlebar-container"
	)
	return title_bar