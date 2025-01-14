# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose the port Dash app runs on
EXPOSE 8050

# Define environment variable for OpenAI API key
ENV OPEN_API_KEY=your_openai_api_key_here

# Run the application
CMD ["python", "app.py"]