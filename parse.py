"""
parse.py

This module handles the natural language processing of invoice data using LangChain and OpenAI.
It provides functionality to:
- Process user queries against scraped invoice data
- Extract specific information from invoice content
- Return structured responses through a Dash callback

The module uses a template-based approach to ensure consistent and focused information extraction
from invoice data, following strict guidelines to return only relevant information.
"""

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
    temperature=0.7  # Lower temperature for more focused, deterministic responses
)

# Initialize chat history for potential future use
chat_history = []

@app.callback(
    Output("llm-response", "children"),
    Input("llm-request-button", "n_clicks"),
    Input("scraped-data", "data"),
    State("llm-request-input", "value"),
)
def handle_llm_request(n_clicks, scraped_data, user_input):
    """
    Process user queries against scraped data and return relevant information.
    
    Args:
        n_clicks (int): Number of times the request button has been clicked
        scraped_data (Union[str, list]): The scraped data to process
        user_input (str): The user's query or information request
    
    Returns:
        dash.html.Div: A formatted HTML div containing the query response or error message
    """
    if n_clicks > 0 and user_input:
        print("LLM Request triggered")

        if not scraped_data:
            print("No scraped data available.")
            return html.Div("No scraped data available to process your request.")
        
        # Process scraped data into a consistent format
        if isinstance(scraped_data, list):
            processed_scraped_data = "\n\n".join(scraped_data)
        else:
            processed_scraped_data = scraped_data
        
        print(f"Processed Scraped Data Length: {len(processed_scraped_data)} characters")

        # Validate processed data
        if not processed_scraped_data:
            return html.Div("No valid data found to process.", style={'color': 'red'})

        try:
            # Define the extraction prompt template with specific instructions
            prompt_template = """
            You are tasked with extracting specific information from the following text content: {processed_scraped_data}
            Please follow these instructions carefully:
            1. **Extract Information:** Only extract the information that directly matches this user query: {user_input}
            2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response
            3. **Empty Response:** If no information matches the query, return an empty string ('')
            4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text
            """

            # Create and execute the LangChain processing pipeline
            prompt = PromptTemplate(
                input_variables=["processed_scraped_data", "user_input"],
                template=prompt_template
            )
            chain = prompt | llm | StrOutputParser()
            result = chain.invoke({
                "processed_scraped_data": processed_scraped_data,
                "user_input": user_input
            })

            # Format and return the response
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
