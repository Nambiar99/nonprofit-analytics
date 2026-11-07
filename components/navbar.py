from dash import html, page_registry
import dash_bootstrap_components as dbc

def create_sidebar():
	new_sidebar = html.Div(
		id="sidebar-container",
		children=[
			html.Div(
				id="sidebar-content",
				children=[
					html.P("Donation Analytics", className="sidebar-title"),
					dbc.Nav(
						[
							dbc.NavLink("Revenue", href="/", active="exact", className="sidebar-options"),
							dbc.NavLink("Donors", href="/donors", active="exact", className="sidebar-options"),
							dbc.NavLink("Campaigns", href="/campaigns", active="exact", className="sidebar-options"),
							dbc.NavLink("Other", href="/other", active="exact", className="sidebar-options"),
						], vertical=True, pills=True, className="sidebar-options"
					)
				]
				)
		], className="sidebar-container"
	)


	return new_sidebar

