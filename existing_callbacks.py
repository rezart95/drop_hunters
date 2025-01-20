from dash import dcc, html, Input, Output, State
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from app import app

@app.callback(
    Output("table-visualization", "children"),
    Output("scraped-data", "data"),
    Input("select-product-button", "n_clicks"),
    State("group-store-input", "value"),
)
def update_table(n_clicks, url):
    """
    Callback function to handle website scraping and data processing when the user clicks
    the select product button.

    Args:
        n_clicks (int): Number of times the button has been clicked. None if never clicked.
        url (str): The URL input by the user to scrape.

    Returns:
        tuple: Contains two elements:
            - html.Div: The visual representation of the scraped data
            - Union[str, List[str], None]: The processed data to store, or None if scraping failed
    """
    if n_clicks is None or n_clicks == 0:
        return (
            html.Div("Please enter a URL and click the button to see the scraped data."),
            None
        )
    
    if not url:
        return (
            html.Div("Please enter a URL and click the button to see the scraped data."),
            None
        )
    
    # Attempt to scrape the website
    html_content = scrape_website(url)
    
    if html_content:
        # Extract and process the content
        body_content = extract_body_content(html_content)
        cleaned_content = clean_body_content(body_content)
        split_contents = split_dom_content(cleaned_content)
        
        # Store the processed data - as a list if split, otherwise as single content
        processed_data = split_contents if len(split_contents) > 1 else cleaned_content
        
        return (
            html.Div([
                html.H5("Scraped Data"),
                html.Pre(cleaned_content)
            ]),
            processed_data
        )
    else:
        return (
            html.Div("Failed to retrieve data from the provided URL."),
            None
        )