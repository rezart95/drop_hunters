from dash import html, Input, Output, State
import openai
import os
from dash_app import app

# Import necessary components from Langchain
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Langchain with OpenAI
llm = ChatOpenAI(
    openai_api_key=os.environ.get('OPEN_API_KEY'),
    model_name="gpt-4o",
    temperature=0.7
)

# Initialize chat history
chat_history = []

@app.callback(
    Output("llm-response", "children"),
    Input("llm-request-button", "n_clicks"),
    State("llm-request-input", "value"),
    Input("scraped-data", "data"),
)
def handle_llm_request(n_clicks, user_input, scraped_data):
    if n_clicks > 0 and user_input:
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

        # Check if there's valid extracted data to proceed
        if not processed_scraped_data:
            return html.Div("No valid data found to process.", style={'color': 'red'})

        try:
            # Use Langchain to process the query
            prompt_template = """
            
            You are tasked with extracting specific information from the following text content: {processed_scraped_data}
            Please follow these instructions carefully:
            1. **Extract Information:** Only extract the information that directly matches this user query: {user_input}
            2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response
            3. **Empty Response:** If no information matches the query, return an empty string ('')
            4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text
            """

            prompt = PromptTemplate(
                input_variables=["processed_scraped_data", "user_input"],
                template=prompt_template
            )
            chain = prompt | llm | StrOutputParser()
            result = chain.invoke({
                "processed_scraped_data": processed_scraped_data,
                "user_input": user_input
            })

            # Display the response in a chat-like format
            return html.Div(
                [
                    html.Div(f"You: {user_input}", style={'font-weight': 'bold'}),
                    html.Div(f"Assistant: {result}")
                ],
                style={"whiteSpace": "pre-wrap"}
            )

        except Exception as e:
            print(f"Error with LLM request: {e}")
            return html.Div("An error occurred while processing your request.")

    return "LLM response will be displayed here."
