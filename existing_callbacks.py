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
    print("Callback triggered")
    print(f"n_clicks: {n_clicks}, url: {url}")
    
    if n_clicks is None or n_clicks == 0:
        print("Button has not been clicked yet.")
        return (
            html.Div("Please enter a URL and click the button to see the scraped data."),
            None
        )
    
    if not url:
        print("URL is empty.")
        return (
            html.Div("Please enter a URL and click the button to see the scraped data."),
            None
        )
    
    print(f"Scraping website: {url}")
    html_content = scrape_website(url)
    print("Scraping completed.")
    
    if html_content:
        print("HTML content retrieved successfully.")
        
        # Extract body content
        body_content = extract_body_content(html_content)
        print("Body content extracted.")
        
        # Clean the body content
        cleaned_content = clean_body_content(body_content)
        print("Body content cleaned.")
        
        # Optionally, split the content if it's too long
        split_contents = split_dom_content(cleaned_content)
        print(f"Content split into {len(split_contents)} parts.")
        
        # Store the processed data
        # If you split the content, you might want to store it as a list
        # Otherwise, store cleaned_content directly
        processed_data = split_contents if len(split_contents) > 1 else cleaned_content
        
        return (
            html.Div([
                html.H5("Scraped Data"),
                html.Pre(cleaned_content)
            ]),
            processed_data
        )
    else:
        print("No content returned from scrape_website.")
        return (
            html.Div("Failed to retrieve data from the provided URL."),
            None
        )