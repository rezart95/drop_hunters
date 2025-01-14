from dash import html, Input, Output, State
from dash_app import app
import layout
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import handle_llm_request

app.layout = layout.layout

@app.callback(
    [Output("table-visualization", "children"),
     Output("scraped-data", "data")],  # Add output for the store
    Input("select-product-button", "n_clicks"),
    Input("group-store-input", "value"),
)
def update_table(n_clicks, url):
    """
    Callback function to handle website scraping and content visualization.
    Also stores the scraped data in dcc.Store component.
    """
    print("Callback triggered")
    print(f"n_clicks: {n_clicks}, url: {url}")
    
    if n_clicks is None:
        print("Button has not been clicked yet.")
        return html.Div("Please enter a URL and click the button to see the scraped data."), None
    
    if n_clicks > 0:
        if not url:
            print("URL is empty.")
            return html.Div("Please enter a URL and click the button to see the scraped data."), None
        
        print("Scraping website...")
        html_content = scrape_website(url)
        print("Scraping completed.")

        if html_content:
            print("HTML content retrieved successfully.")
            body_content = extract_body_content(html_content)
            cleaned_content = clean_body_content(body_content)
            dom_chunks = split_dom_content(cleaned_content)
            print("DOM chunks created.")
            
            # Store the complete content for LLM processing
            stored_content = "\n".join(dom_chunks)
            
            return (
                html.Div([
                    html.H5("Scraped Data"),
                    html.Pre("\n".join(dom_chunks), style={"maxHeight": "200px", "overflowY": "auto"})
                ]),
                stored_content  # This will be stored in dcc.Store
            )
        else:
            print("No content returned from scrape_website.")
            return html.Div("Failed to retrieve data from the provided URL."), None
    
    return html.Div("Please enter a URL and click the button to see the scraped data."), None

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)