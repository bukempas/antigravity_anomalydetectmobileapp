import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession, Part, Tool
import vertexai.preview.generative_models as generative_models
app = Flask(__name__)
CORS(app)  # Enable CORS for mobile app communication
# Initialize Vertex AI
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "your-project-id")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
try:
    vertexai.init(project=PROJECT_ID, location=LOCATION)
except Exception as e:
    print(f"Error initializing Vertex AI: {e}")
# --- Tool Definitions ---
# def report_anomaly(issue_type: str, severity: str, description: str, location: str):
#     """Reports a city maintenance issue or anomaly to the municipality."""
#     print(f"🚨 [MUNICIPALITY REPORT] Type: {issue_type} | Severity: {severity} | Desc: {description}")
#     return {"status": "success", "ticket_id": "ADM-AUTO-4291", "message": "Report submitted successfully."}
# Create the Tool
# anomaly_tool = Tool.from_function(report_anomaly)
# Initialize Model with Tools
# Using gemini-1.5-flash for speed and multimodal capabilities
try:
    # vertexai.init(project=PROJECT_ID, location=LOCATION)
    # model = GenerativeModel("gemini-1.5-flash-001", tools=[anomaly_tool])
    # chat = model.start_chat()
    model = None # Force mock mode
    chat = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    chat = None
@app.route('/chat', methods=['POST'])
def chat_endpoint():
    # Handle Multipart Request (Image + Text)
    user_message = request.form.get('message', '')
    image_file = request.files.get('image')
    if not model:
        # Fallback for demo/simulation purposes if credentials aren't set
        import time
        time.sleep(1) # Simulate network delay
        mock_response = "I am currently in demo mode (Vertex AI not connected). But if I were connected, I would answer your question about Abu Dhabi or process your anomaly report! 🌴"
        if "pothole" in user_message.lower() or (image_file and "pothole" in image_file.filename.lower()):
             mock_response = "🚨 Report Filed. I have identified a pothole (Severity: Medium) and notified the Abu Dhabi Municipality. Ticket #ADM-DEMO-123."
        return jsonify({"response": mock_response})
    if not user_message and not image_file:
        return jsonify({"error": "No message or image provided"}), 400
    try:
        parts = []
        if user_message:
            parts.append(Part.from_text(user_message))
        
        if image_file:
            image_bytes = image_file.read()
            parts.append(Part.from_data(data=image_bytes, mime_type=image_file.mimetype))
        # Send message to agent
        response = chat.send_message(parts)
        
        # Check for function calls
        response_text = ""
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.function_call:
                    pass
                if part.text:
                    response_text += part.text
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error generating response: {e}")
        return jsonify({"error": f"Failed to generate response: {str(e)}"}), 500
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
