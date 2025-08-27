# Complete Voice Assistant

This project is a fully functional, voice-controlled assistant that runs as a web application. It listens to a user's spoken question, processes it with a powerful Large Language Model (LLM) to generate an intelligent response, and then speaks the answer back to the user.

## Features

- 🎤 **Speech-to-Text**: Utilizes OpenAI's Whisper model to accurately transcribe voice input from the user's microphone.
- 🧠 **Intelligent Responses**: Integrates with IBM WatsonX's mistral-large model to understand user queries and generate thoughtful, context-aware answers.
- 🗣️ **Text-to-Speech**: Uses Google's Text-to-Speech engine to convert the AI's text response back into spoken audio.
- 🌐 **Web Interface**: Built with Gradio to provide a simple and interactive user interface that runs in a web browser.

## Tech Stack

- Python 3.11+
- Gradio: For the web user interface.
- openai-whisper: For speech-to-text.
- ibm-watson-machine-learning: For connecting to the WatsonX LLM.
- python-dotenv: For managing API keys securely.
- gTTS (Google Text-to-Speech): For text-to-speech.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Clone the Repository

```bash
git clone <your-repository-url>
cd voice-assistant
```

Or simply download the code and place it in a folder named `voice-assistant`.

### Create and Activate a Virtual Environment

On Windows:

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

### Install Dependencies

All required libraries are listed in the `requirements.txt` file. Install them with a single command:

```bash
pip install -r requirements.txt
```

### Configuration

Before running the application, you need to provide your IBM WatsonX API credentials.

1. Create a new file in the main project folder named `.env`.
2. Add your credentials to the `.env` file in the following format:

```
WATSONX_API_KEY="your_api_key_here"
WATSONX_PROJECT_ID="your_project_id_here"
```

## Usage

Once the setup and configuration are complete, run the application from your terminal:

```bash
python app.py
```

The terminal will provide a local URL (e.g., `http://127.0.0.1:7860`). Open this link in your web browser to start using the voice assistant.