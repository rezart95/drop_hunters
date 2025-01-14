from dash import html, Input, Output, State
import openai
import os
from app import app

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPEN_API_KEY")

@app.callback(
    Output("llm-response", "children"),
    Input("llm-request-button", "n_clicks"),
    State("llm-request-input", "value"),
    Input("scraped-data", "data"),
)
def handle_llm_request(n_clicks, llm_request, scraped_data):
    if n_clicks > 0 and llm_request:
        print("LLM Request triggered")

        if not scraped_data:
            print("No scraped data available.")
            return html.Div("No scraped data available to process your request.")
        
        # If scraped_data is a list (split content), join it
        if isinstance(scraped_data, list):
            processed_scraped_data = "\n\n".join(scraped_data)
        else:
            processed_scraped_data = scraped_data
        
        print(f"Processed Scraped Data Length: {len(processed_scraped_data)} characters")
        
        # Prepare the conversation history with the scraped data
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"{llm_request}\n\nScraped Data:\n{processed_scraped_data}"
            }
        ]

        try:
            # Call the LLM (using OpenAI's ChatCompletion)
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # Ensure the model name is correct
                messages=conversation,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.7,
            )

            llm_response_text = response.choices[0].message.content.strip()
            print("LLM Response received.")

            # Display the response in a chat-like format
            return html.Div(
                [
                    html.Strong("LLM Response:"),
                    html.P(llm_response_text)
                ],
                style={"whiteSpace": "pre-wrap"}
            )

        except Exception as e:
            print(f"Error with LLM request: {e}")
            return html.Div("An error occurred while processing your request.")

    return "LLM response will be displayed here."