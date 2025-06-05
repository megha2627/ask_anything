# AskAnything - Simple AI Chat App with Flask

A basic web application built using **Flask** and **Hugging Face Transformers** that lets users ask questions and get AI-generated answers in real-time.

---

## Features

- User-friendly web interface to enter questions
- Uses a pre-trained AI language model (GPT-2) to generate responses
- Displays AI answers dynamically on the webpage
- Simple and easy to understand for beginners learning Flask and AI integration

---

## Technologies Used

- **Flask**: Python web framework to build the backend and serve webpages
- **Transformers**: Hugging Face library to load and run AI models
- **PyTorch (torch)**: Deep learning framework powering the AI model computations
- **HTML + Jinja2**: Frontend template rendering

---

## Installation

1. Clone this repository:

   
(Optional but recommended) Create and activate a virtual environment:
bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
python -m pip install flask transformers torch
Usage
Run the Flask app:

bash
python app.py
Open your browser and go to:
http://127.0.0.1:5000

Type any question and press Ask to get an AI-generated answer.

Project Structure
csharp
Copy
Edit
ask_anything/
├── app.py           # Flask backend application
├── templates/
│   └── index.html   # Frontend HTML template
└── static/          # (Optional) CSS or JS files
How It Works
Flask serves a webpage with a form to input questions.

When the form is submitted, Flask sends the question to the AI model (GPT-2) using the Hugging Face transformers pipeline.

The AI model generates a response and Flask returns it back to the webpage.

The response is dynamically displayed using Jinja2 templating.

