# Automated Legal Document Analyzer

## Overview
The Automated Legal Document Analyzer is an AI-powered web application that analyzes legal documents and generates easy-to-understand summaries using a locally running language model.

## Features
- Analyze legal document text.
- Generate AI-powered explanations and summaries.
- Simple web interface built with HTML and CSS.
- Flask backend for processing user input.
- Local AI processing using Ollama.

## Technologies Used
- Python
- Flask
- HTML and CSS
- Ollama
- Llama 3.2 (1B)

## Requirements
- Python
- Ollama
- A locally downloaded `llama3.2:1b` model

## How to Run

1. Install Python and Ollama.
2. Download the model:

   `ollama pull llama3.2:1b`

3. Install dependencies:

   `pip install -r requirements.txt`

4. Start the application:

   `python app.py`

5. Open `http://127.0.0.1:5000` in your browser.

## Disclaimer
This project is for educational purposes only. AI-generated analysis may be inaccurate and is not a substitute for professional legal advice.

## Author
Jerush
