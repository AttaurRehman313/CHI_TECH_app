import google.generativeai as genai
from dotenv import load_dotenv
import base64
import os


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyAB85KditGJByZ2wlh0MjF5Ry7vzH1e5zo")

def image_text(image_path):
  model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp") 

  with open(image_path, 'rb') as image_file:
        binary_data = image_file.read()
  encoded_image = encoded_image = base64.b64encode(binary_data).decode("utf-8")

  prompt = """Summarize all the text in the image. The summary should focus on a complete and logical flow, including the sequence of events or concepts presented visually in the image."""

  response = model.generate_content([{'mime_type': 'image/jpeg', 'data': encoded_image}, prompt])

#   print(response.text)
  return response.text