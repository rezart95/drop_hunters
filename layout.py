from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1
                        ([
                            html.Span("Welcome"),
                            html.Br(),
                            html.Span("to DropHunters"),
                        ]),
                        html.P("Get all the latest drops and releases from your favorite brands."),
                ],
                style={"vertical-alignment": "top", "height": 260,}
                ), 
                html.Div(
                    [
                        html.Div(style={'width': 206}),
                        html.Div(style={'width': 104})
                    ],
                    style={'margin-left': 15, 'margin-right': 15, 'display': 'flex'}
                ),
                html.Div(
                    [
                        html.Div(dbc.RadioItems(
                            className='btn-group',
                            inputClassName='btn-check',
                            labelClassName="btn btn-outline-light",
                            labelCheckedClassName="btn btn-light",
                            options=[
                                {"label": "Graph", "value": 1}, 
                                {"label": "Table", "value": 2}
                            ],
                            value=1
                        ),
                                style={'width': 206}),
                        html.Div(dbc.Button(
                            "About",
                            className="btn btn-info",
                            n_clicks=0
                        ), 
                                style={'width': 104})
                    ],
                    style={
                        'margin-left': 15,
                        'margin-right': 15,
                        'display': 'flex'
                    }
                ),
                html.Div([
                    html.Div([
                        html.H2('Unclearable Dropdown:'),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Option A', 'value': 1}, 
                                {'label': 'Option B', 'value': 2}, 
                                {'label': 'Option C', 'value': 3}
                            ],
                            value=1,
                            clearable=False,
                            optionHeight=40
                        )
                    ]),
                    html.Div([
                        html.H2('Unclearable Dropdown:'),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Option A', 'value': 1}, 
                                {'label': 'Option B', 'value': 2}, 
                                {'label': 'Option C', 'value': 3}
                            ],
                            value=2,
                            clearable=False,
                            optionHeight=40
                        )
                    ]),
                    html.Div([
                        html.H2('Clearable Dropdown:'),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Option A', 'value': 1}, 
                                {'label': 'Option B', 'value': 2}, 
                                {'label': 'Option C', 'value': 3}
                            ],
                            clearable=True,
                            optionHeight=40
                        )
                    ]),
                ],
                style={'margin-left': 15, 'margin-right': 15, 'margin-top': 30}),
            ],
            style={'width': 340, 'margin-left': 35, 'margin-top': 35, 'margin-bottom': 35}
        ),
        html.Div(
            [
                html.Div(style={'width': 790}),
                html.Div(style={'width': 200})
            ],
            style={
                'width': 990,
                'margin-top': 35,
                'margin-right': 35,
                'margin-bottom': 35,
                'display': 'flex'
                }
        )
    ],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')