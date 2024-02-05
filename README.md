# convogem
# Streamlit App with Docker Deployment

This project is a Streamlit app that utilizes Docker for deployment. The app allows users to interact with a GPT-4-powered chatbot.

## Table of Contents

- [Installation and Usage](#installation)
- [Docker Deployment](#docker-deployment)

## Installation and Usage

Install the gpt4all-j model from: https://drive.google.com/file/d/1owOS6ITGPuVBR7JFuWX9fiD0YFo4tpGP/view?usp=drive_link

1. Clone the repository:

   ```bash
   git clone https://github.com/Spandanachereddy/convogem.git
   cd convogem

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

3. Run

   ```bash
   streamlit run app.py

## Docker Deployment

1. Build the Docker image from the project directory:

   ```bash
   docker build -t convogem:latest .

2. Running the Docker Container

   ````bash
   docker run -p 8501:8501 convogem:latest

Access the deployed app in your web browser at http://localhost:8501.



