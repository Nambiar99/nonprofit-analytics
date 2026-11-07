import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
import dash

import os
from dotenv import load_dotenv
load_dotenv()

from components.navbar import create_sidebar
from components.titlebar import create_title_bar
from components.callbacks import register_app_callbacks

app = Dash(
	__name__,
	use_pages=True,
	external_stylesheets=[dbc.themes.BOOTSTRAP],
	suppress_callback_exceptions=True
)

server = app.server

register_app_callbacks(app)

app.layout = dbc.Container([
	dbc.Row([create_title_bar()]),
	dbc.Row([
		dbc.Container(page_container, fluid=True)
	])
], fluid=True, className="page-container")

if __name__ == "__main__":
	port = os.getenv("PORT")
	app.run(host="0.0.0.0", debug=False, port=port)
