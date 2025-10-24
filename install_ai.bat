@echo off
echo Installing DeepFace AI with TensorFlow CPU (Recommended for Windows)
echo ==========================================

echo Step 1: Creating Python virtual environment...
python -m venv deepface_env
call deepface_env\Scripts\activate

echo Step 2: Installing TensorFlow CPU (lighter version)...
pip install tensorflow-cpu==2.13.0

echo Step 3: Installing DeepFace and dependencies...
pip install deepface==0.0.79
pip install flask==2.3.3
pip install flask-cors==4.0.0
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install pillow==10.0.0

echo Step 4: Installation complete!
echo.
echo To start the AI server:
echo    deepface_env\Scripts\activate
echo    python api_server.py
echo.
echo Press any key to exit...
pause >nul
