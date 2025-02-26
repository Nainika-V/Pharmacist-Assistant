# Pharmacist-Assistant
# Overview
The Pharmacist Assistant is a web-based tool that extracts and enhances handwritten prescription text using Google AI Studio's Gemini model. It helps pharmacists accurately read prescriptions, reducing errors and improving efficiency.

# Features
   Image Capture – Take a picture of handwritten prescriptions.
   
   Image Preprocessing – Enhances clarity for better recognition.
   
   AI-powered Text Extraction – Uses Google Gemini AI for accurate text interpretation.
   
   Secure & Private – No patient data storage and API keys are secured.

# Tech Stack
Frontend: HTML, JavaScript (for UI & camera integration)

Backend: Flask (Python)

AI Model: Gemini 1.5 (via Google AI Studio API)

Image Processing: PIL (Python Imaging Library)

# How It Works
User captures a prescription image via the camera.

Image is preprocessed (grayscale conversion, sharpening, contrast enhancement).

AI extracts and corrects the handwritten text.

The pharmacist receives the processed text output.

# Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/Nainika-V/Pharmacist-Assistant.git  

cd Pharmacist-Assistant  

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv  

source venv/bin/activate  # Mac/Linux  

venv\Scripts\activate  # Windows 

3️⃣ Install Dependencies

pip install -r requirements.txt  

4️⃣ Set Up Environment Variables

Create a .env file in the project directory.

Add your Google AI API key inside it:

GOOGLE_AI_API_KEY=your_actual_api_key_here

5️⃣ Run the Application

python app.py  

6️⃣ Access the Web App

http://127.0.0.1:5000  

# Future Enhancements
   Integration with pharmacy databases for real-time drug suggestions
   
   Mobile-friendly UI
