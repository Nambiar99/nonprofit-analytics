from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

def metric_card(
	card_id: str,
	title: str,
	value: float,
	delta=None,
	color="primary",
):
	card = dbc.Card(
		dbc.CardBody([
			html.H6(str(title), className="card-title"),
			html.H2(value, id=card_id, className="card-value"),
		]), className="metric-card"
	)
	return card