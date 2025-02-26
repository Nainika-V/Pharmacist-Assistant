from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from PIL import Image, ImageEnhance, ImageFilter
import io
import base64
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load environment variables from .env file
load_dotenv()

# Access the API key securely
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")

# Configure Google AI with the secure key
genai.configure(api_key=GOOGLE_AI_API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

# Convert Image to Base64
def encode_image(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    return base64.b64encode(img_byte_arr.getvalue()).decode("utf-8")

# Preprocess Image for Better Text Recognition
def preprocess_image(image):
    image = image.convert("L")  # Grayscale
    image = image.filter(ImageFilter.SHARPEN)
    image = ImageEnhance.Contrast(image).enhance(2)
    image = image.resize((image.width * 2, image.height * 2))
    return image

# Process Image with Gemini AI
def process_image_with_gemini(image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([
        "Extract text from this prescription image accurately. The text is handwritten, so focus on improving clarity. If the text is unclear, make an educated guess based on common medical prescriptions:",
        {"mime_type": "image/png", "data": encode_image(image)}
    ])
    return response.text.strip()

@app.route('/process_prescription', methods=['POST'])
def process_prescription():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    try:
        image = Image.open(image_file)
        image = preprocess_image(image)  # Apply preprocessing
        extracted_text = process_image_with_gemini(image)  # Send to Gemini

        return jsonify({"corrected_text": extracted_text})
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
