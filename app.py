from flask import Flask, request, jsonify
import vertexai
from vertexai.preview.generative_models import GenerativeModel
import google.auth
from google.oauth2 import service_account

app = Flask(__name__)

# Replace this with your actual path to the service account key file
SERVICE_ACCOUNT_FILE = "service_account_key.json"

# Replace with your GCP project ID and location
PROJECT_ID = "your-gcp-project-id"
LOCATION = "us-central1"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

model = GenerativeModel("gemini-1.5-pro")

@app.route("/verify-news", methods=["POST"])
def verify_news():
    data = request.json
    news_text = data.get("text", "")
    if not news_text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"You are a fake news checker AI. Classify this as REAL, FAKE, or UNVERIFIABLE and explain briefly:

"{news_text}""
    response = model.generate_content(prompt)
    return jsonify({"verdict": response.text.strip()}), 200

if __name__ == "__main__":
    app.run(debug=True)
