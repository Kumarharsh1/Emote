# DeepFace AI Setup Instructions

## Step 1: Install Python Dependencies
Open Command Prompt or PowerShell and run:

\\\ash
# First install Python 3.8+ if you don't have it
# Then install the dependencies:
pip install -r requirements.txt
\\\

## Step 2: Start the Flask API Server
\\\ash
python api_server.py
\\\

The server will start at: http://127.0.0.1:5000

## Step 3: Update API URL in React App
Make sure the API_BASE_URL in Scanner.jsx points to your Flask server:
\\\javascript
const API_BASE_URL = "http://localhost:5000";
\\\

## Step 4: Test the API
Visit: http://127.0.0.1:5000/api/health

You should see: {"status":"healthy","message":"Face analysis API is running"}

## Troubleshooting:
1. **TensorFlow Installation Issues**:
   \\\ash
   # If TensorFlow fails, try CPU-only version:
   pip uninstall tensorflow
   pip install tensorflow-cpu==2.13.0
   \\\

2. **Port Already in Use**:
   \\\ash
   # Change port in api_server.py:
   app.run(host="127.0.0.1", port=5001, debug=True)
   \\\

3. **DeepFace Model Download**:
   - First run will download pre-trained models (~500MB)
   - Ensure stable internet connection

## Features:
- ✅ High-accuracy emotion detection (7 emotions)
- ✅ Precise gender classification 
- ✅ Face detection and alignment
- ✅ Confidence scores for both gender and emotion
- ✅ Professional neural network models
