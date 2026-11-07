from dash import Dash, html, dcc
import datetime

def date_input(
	input_id: str,
	label_text: str = "Select Date:",
	default_date=None,
	min_date_allowed=None,
	max_date_allowed=None,
):
	if default_date is None:
		default_date = datetime.date.today()
	return html.Div(
		[
			html.Label(label_text, htmlFor=input_id, className="comp-label"),
			dcc.DatePickerSingle(
				id=input_id,
				date=default_date,
				min_date_allowed=min_date_allowed,
				max_date_allowed=max_date_allowed,
				display_format="YYYY-MM-DD",
			), 
		], className="comp-main"
	)

def dropdown_input(
	input_id: str,
	options: list,
	label_text: str = "Select Options:",
	default_value=None,
	placeholder: str = "Select...",
	multi: bool = True,
):
	return html.Div(
		[
			html.Label(label_text, htmlFor=input_id, className="comp-label"),
			dcc.Dropdown(
				id=input_id,
				options=options,
				value=default_value,
				multi=multi,
				placeholder=placeholder,
			)
		], className="comp-main"
	)