import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


# Sample brand options; replace with dynamic data as needed
brand_options = [
    {"label": "Brand A", "value": "brand_a"},
    {"label": "Brand B", "value": "brand_b"},
    {"label": "Brand C", "value": "brand_c"},
]

# Sample size options; replace with dynamic data as needed
size_options = [
    {"label": "Small", "value": "S"},
    {"label": "Medium", "value": "M"},
    {"label": "Large", "value": "L"},
    {"label": "Extra Large", "value": "XL"},
]

navbar = dbc.Navbar(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.NavbarBrand(
                                "Drop Hunters", 
                                className="ms-2",
                                style={"fontSize": "1.5rem"}
                            ),
                        ), 
                    ],
                    align="center",
                )
            ],
            fluid=True,
        )
    ],
    color="azure",
    fixed="top",
)


layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                # Side Panel
                dbc.Col(
                    [
                        html.Div(style={"marginTop": "60px"}),
                        html.H5(
                            "Select Brands", 
                            # style={"fontSize": "1.25rem"}, 
                            className="sidebar-title"
                        ),
                        dcc.Dropdown(
                            id="brand-dropdown",
                            options=brand_options,
                            multi=True,
                            placeholder="Select brands",
                            className="sidebar-dropdown",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    style={"marginTop": "80px"}),
                                html.H5(
                                    "Choose Payment Method", 
                                    # style={"fontSize": "1.25rem"}, 
                                    className="sidebar-title"
                                ),
                                dbc.RadioItems(
                                    id="payment-method",
                                    options=[
                                        {"label": "Google Pay", "value": "google_pay"},
                                        {"label": "Apple Pay", "value": "apple_pay"},
                                        {"label": "Paypal", "value": "paypal"},
                                    ],
                                    value="google_pay",
                                    inline=False,
                                ),
                            ],
                            style={"textAlign": "left"}
                        ),
                    ],
                    width=3,
                    className="sidebar",
                    style={"borderRight": "5px solid #DCDCDC"},  # Added border to separate from main content
                ),
                # Main Content
                dbc.Col(
                    [
                        html.Div(style={"marginTop": "60px"}),  # Adds space below the navbar
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    label="Existing Products",
                                    children=[
                                        html.Pre(),
                                        html.H5(
                                            "Product Link", 
                                            # style={"fontSize": "1.25rem"},
                                            className="sidebar-title"
                                        ),
                                        html.Div(
                                            children=[
                                                dcc.Input(
                                                    id="group-store-input",
                                                    placeholder="Enter URL",
                                                    style={"margin-right": "10px", "width": "80%"},
                                                ),
                                                html.Button(
                                                    id="select-product-button",
                                                    n_clicks=0,
                                                    children="Select Product",
                                                    className="regular-button",
                                                    style={'margin-left': '1%', 'display': 'inline-block', "width": "15%"},
                                                ),
                                            ]
                                        ),
                                        dbc.CardGroup(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(style={"marginTop": "30px"}),
                                                        html.H5(
                                                            "Select Category", 
                                                            # style={"fontSize": "1.25rem"}, 
                                                            className="sidebar-title"
                                                        ),
                                                        dbc.RadioItems(
                                                            id="category-radio",
                                                            options=[
                                                                {"label": "Clothes", "value": "clothes"},
                                                                {"label": "Shoes", "value": "shoes"},
                                                                {"label": "Accessories", "value": "accessories"},
                                                            ],
                                                            value="clothes",
                                                            inline=True,
                                                        ),
                                                    ],
                                                    style={"textAlign": "left"}
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                html.H5(
                                                    "Select Product Size", 
                                                    # style={"fontSize": "1.25rem"}, 
                                                    className="sidebar-title"
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        html.Div(
                                            dcc.Dropdown(
                                                id="size-dropdown",
                                                options=size_options,
                                                placeholder="Select size",
                                                className="sidebar-dropdown",
                                                style={"width": "90%"}  # Regulating the width
                                            ),
                                            style={"textAlign": "left"}
                                        ),
                                    ],
                                    tab_id="existing-products",
                                ),
                                dbc.Tab(
                                    label="New Releases",
                                    children=[
                                        dbc.CardGroup(
                                            [
                                                html.H5("Upload Product Image"),
                                                dcc.Upload(
                                                    id="upload-data",
                                                    children=html.Div(["Drag and Drop or Select File"]),
                                                    multiple=False,
                                                    accept=".xlsx,.csv"
                                                ),
                                                dbc.Tooltip(
                                                    "Supported file format: .jpg or .png",
                                                    target="upload-data",
                                                    style={"margin-left": "5px"},
                                                    autohide=False
                                                ),
                                                dcc.Loading(
                                                    id="data-loading-viz-pre",
                                                    type="default",
                                                    children=html.Div(id="filecache_marker", style={"display": "none"}),
                                                ),
                                                # html.Div(
                                                #     id="uploaded-file-name-div",
                                                #     children=[],
                                                #     style={"display": "none"},
                                                # ),
                                                dbc.Alert(
                                                    "File size exceeds 5MB limit, please upload a smaller file",
                                                    id="file-size-error",
                                                    color="danger",
                                                    style={"display": "none"}
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                html.H5("Product Description"),
                                                dbc.Textarea(
                                                    id="product-description",
                                                    placeholder="Describe the product...",
                                                    style={"height": "100px"},
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        html.Div(
                                            [
                                                html.H5("Select Date and Time"),
                                                html.Div(
                                                    style={"display": "flex", "alignItems": "center"},
                                                    children=[
                                                        dcc.DatePickerSingle(
                                                            id="available-date",
                                                            date=None,
                                                            display_format="DD/MM/YYYY",
                                                            className="SingleDatePickerInput__withBorder"
                                                        ),
                                                        html.Div(style={"width": "10px"}),  # Spacer
                                                        dmc.TimeInput(w=100),
                                                    ]
                                                ),
                                            ],
                                            className="date-picker-group",
                                        ),
                                    ],
                                    tab_id="new-releases",
                                ),
                            ],
                            id="tabs",
                            active_tab="existing-products",
                        ),
                    ],
                    width=9,
                ),
            ],
            className="main-row",
        )
    ],
    fluid=True,
    className="dashboard-container",
)