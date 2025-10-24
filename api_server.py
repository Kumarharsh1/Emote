from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
from analyze_face import analyze_face

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/api/analyze-face", methods=["POST"])
def analyze_face_api():
    try:
        # Check if the post request has the file part
        if "image" not in request.files:
            return jsonify({"success": False, "error": "No image file provided"}), 400
        
        file = request.files["image"]
        
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == "":
            return jsonify({"success": False, "error": "No file selected"}), 400
        
        if file and allowed_file(file.filename):
            # Generate unique filename
            filename = str(uuid.uuid4()) + "_" + secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            
            # Save the file
            file.save(filepath)
            
            try:
                # Analyze the face
                result = analyze_face(filepath)
                
                # Clean up: delete the uploaded file after analysis
                try:
                    os.remove(filepath)
                except:
                    pass  # Ignore cleanup errors
                
                return jsonify(result)
                
            except Exception as e:
                # Clean up on error
                try:
                    os.remove(filepath)
                except:
                    pass
                return jsonify({"success": False, "error": f"Analysis failed: {str(e)}"}), 500
        
        return jsonify({"success": False, "error": "Invalid file type. Allowed: png, jpg, jpeg, gif, bmp"}), 400
        
    except Exception as e:
        return jsonify({"success": False, "error": f"Server error: {str(e)}"}), 500

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "Face analysis API is running"})

if __name__ == "__main__":
    print("Starting Face Analysis API Server...")
    print("Make sure you have installed: pip install flask flask-cors deepface")
    app.run(host="127.0.0.1", port=5000, debug=True)
