from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

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

layout = dbc.Container(
    [
        dbc.Row(
            [
                # Side Panel
                dbc.Col(
                    [
                        html.H2("Brands", className="sidebar-title"),
                        dcc.Dropdown(
                            id="brand-dropdown",
                            options=brand_options,
                            multi=True,
                            placeholder="Select brands",
                            className="sidebar-dropdown",
                        ),
                    ],
                    width=3,
                    className="sidebar",
                ),
                # Main Content
                dbc.Col(
                    [
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    label="Existing Products",
                                    children=[
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Product Link"),
                                                dbc.Input(
                                                    type="url",
                                                    id="product-link",
                                                    placeholder="Enter product URL",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Category"),
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
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Size"),
                                                dcc.Dropdown(
                                                    id="size-dropdown",
                                                    options=size_options,
                                                    placeholder="Select size",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                    ],
                                    tab_id="existing-products",
                                ),
                                dbc.Tab(
                                    label="New Releases",
                                    children=[
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Upload Product Image"),
                                                dcc.Upload(
                                                    id="product-upload",
                                                    children=html.Div(
                                                        [
                                                            "Drag and Drop or ",
                                                            html.A("Select Files"),
                                                        ]
                                                    ),
                                                    style={
                                                        "width": "100%",
                                                        "height": "60px",
                                                        "lineHeight": "60px",
                                                        "borderWidth": "1px",
                                                        "borderStyle": "dashed",
                                                        "borderRadius": "5px",
                                                        "textAlign": "center",
                                                        "margin-bottom": "15px",
                                                    },
                                                    multiple=False,
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Product Description"),
                                                dbc.Textarea(
                                                    id="product-description",
                                                    placeholder="Describe the product...",
                                                    style={"height": "100px"},
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        dbc.CardGroup(
                                            [
                                                dbc.Label("Available Date"),
                                                dcc.DatePickerSingle(
                                                    id="available-date",
                                                    date=None,
                                                    display_format="DD/MM/YYYY",
                                                ),
                                            ],
                                            className="mb-3",
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