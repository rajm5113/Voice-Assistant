import gradio as gr
import whisper
import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model
from gtts import gTTS
import io

# --- Part 1: Load Secrets and AI Models ---
print("Loading models and secrets...")
load_dotenv()
api_key = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")

whisper_model = whisper.load_model("base")

# --- Part 2: Configure Watsonx LLM ---
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}
model_params = {
    "decoding_method": "greedy",
    "max_new_tokens": 400, # Increased token limit for longer answers
    "repetition_penalty": 1
}
mistral_model = Model(
    model_id="mistralai/mistral-large",
    params=model_params,
    credentials=credentials,
    project_id=project_id
)
print("Models loaded successfully!")

# --- Part 3: The Main Function ---
def voice_assistant_pipeline(audio_filepath):
    """
    The full pipeline: Speech-to-Text -> LLM -> Text-to-Speech
    """
    if audio_filepath is None:
        return "Please record audio first.", "", None

    # Step 1: Transcribe audio to text (Listen)
    transcription_result = whisper_model.transcribe(audio_filepath, fp16=False)
    transcribed_text = transcription_result["text"]
    
    # Step 2: Send text to the LLM (Think)
    response_text = mistral_model.generate_text(prompt=transcribed_text)
    
    # Step 3: Convert the LLM's response text to speech (Speak)
    tts = gTTS(response_text, lang='en')
    tts.save("response.mp3")
    
    return transcribed_text, response_text, "response.mp3"

# --- Part 4: Create the User Interface ---
iface = gr.Interface(
    fn=voice_assistant_pipeline,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=[
        gr.Textbox(label="You Said:"),
        # This is the line we changed to add the scrollbar
        gr.Textbox(label="Assistant Said:", lines=10),
        gr.Audio(label="Assistant's Voice", type="filepath", autoplay=True)
    ],
    title="Complete Voice Assistant",
    description="Ask a question, and the assistant will listen, think, and speak its response."
)

iface.launch(server_name="0.0.0.0", server_port=8080)