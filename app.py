from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import layout
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout.layout


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
            body_content = extract_body_content(html_content)
            cleaned_content = clean_body_content(body_content)
            dom_chunks = split_dom_content(cleaned_content)
            print("DOM chunks created.")
            return html.Div([
                html.H5("Scraped Data"),
                html.Pre("\n".join(dom_chunks), style={"maxHeight": "200px", "overflowY": "auto"})
            ])
        else:
            print("No content returned from scrape_website.")
            return html.Div("Failed to retrieve data from the provided URL.")
    
    return html.Div("Please enter a URL and click the button to see the scraped data.")

from dash import html, Input, Output, State
import openai
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPEN_API_KEY")

@app.callback(
    Output("llm-response", "children"),
    Input("llm-request-button", "n_clicks"),
    State("llm-request-input", "value"),
    State("table-visualization", "children"),
)
def handle_llm_request(n_clicks, llm_request, table_content):
    if n_clicks > 0 and llm_request:
        print("LLM Request triggered")
        
        # Extract the scraped data from table_content
        scraped_data = ""
        for component in table_content.get("children", []):
            if isinstance(component, html.Pre):
                scraped_data += component.children + "\n"
        
        # Prepare the prompt for the LLM
        prompt = f"{llm_request}\n\nScraped Data:\n{scraped_data}"
        
        try:
            # Call the LLM (assuming OpenAI)
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            
            llm_response_text = response.choices[0].message.content.strip()
            
            # Convert the response to a table format if applicable
            # For simplicity, we'll display it as plain text
            return html.Pre(llm_response_text)
        
        except Exception as e:
            print(f"Error with LLM request: {e}")
            return html.Div("An error occurred while processing your request.")
    
    return "LLM response will be displayed here."




if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

# if __name__ == "__main__":
#     app.run_server(host="0.0.0.0", port=8050, debug=True)