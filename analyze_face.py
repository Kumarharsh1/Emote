from deepface import DeepFace
import sys
import json
import os

def analyze_face(image_path):
    try:
        print(f"Analyzing image: {image_path}")
        
        # Verify the image file exists
        if not os.path.exists(image_path):
            return {"success": False, "error": f"Image file not found: {image_path}"}
        
        # Analyze the image for gender and emotion
        analysis = DeepFace.analyze(
            img_path=image_path,
            actions=["gender", "emotion"],
            detector_backend="retinaface",  # Use a more accurate detector
            align=True,  # Perform alignment for better accuracy
            silent=True  # Suppress verbose output
        )
        
        # The result is a list of analyses for each face found. We take the first one.
        result = analysis[0]
        
        print(f"Analysis successful: {result['dominant_emotion']} emotion, {result['dominant_gender']} gender")
        
        # Format the result
        return {
            "emotion": result["dominant_emotion"],
            "emotion_confidence": round(result["emotion"][result["dominant_emotion"]], 2),
            "gender": result["dominant_gender"],
            "gender_confidence": round(result["gender"][result["dominant_gender"]], 2),
            "success": True
        }
    except Exception as e:
        error_msg = f"DeepFace analysis error: {str(e)}"
        print(error_msg)
        return {"success": False, "error": error_msg}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"success": False, "error": "Usage: python analyze_face.py <image_path>"}))
        sys.exit(1)
    
    image_path = sys.argv[1]
    result = analyze_face(image_path)
    print(json.dumps(result))
