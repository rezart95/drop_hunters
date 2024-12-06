from dash import dcc, html, Input, Output
from scrape import scrape_website
from app import app

@app.callback(
    Output("table-visualization", "children"),
    Input("select-product-button", "n_clicks"),
    Input("group-store-input", "value"),
)
def update_table(n_clicks, url):
    print("Callback triggered")
    print(f"n_clicks: {n_clicks}, url: {url}")
    
    if n_clicks is None:
        print("Button has not been clicked yet.")
        return html.Div("Please enter a URL and click the button to see the scraped data.")
    
    if n_clicks > 0:
        if not url:
            print("URL is empty.")
            return html.Div("Please enter a URL and click the button to see the scraped data.")
        
        print("Scraping website...")
        html_content = scrape_website(url)
        print("Scraping completed.")

        if html_content:
            print("HTML content retrieved successfully.")
            return html.Div([
                html.H5("Scraped Data"),
                html.Pre(html_content)
            ])
        else:
            print("No content returned from scrape_website.")
            return html.Div("Failed to retrieve data from the provided URL.")
    
    return html.Div("Please enter a URL and click the button to see the scraped data.")