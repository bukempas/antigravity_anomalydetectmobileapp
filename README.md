# Agentic Mobile App (Flutter + Python ADK)
This project demonstrates a mobile app that uses a Python backend powered by Google's Agent Development Kit (ADK) / Vertex AI to answer questions about Abu Dhabi and GovAI.

"Google Cloud credits are provided for this project." #AISprint

## Prerequisites
- **Flutter SDK**: [Install Flutter](https://docs.flutter.dev/get-started/install)
- **Python 3.8+**: [Install Python](https://www.python.org/downloads/)
- **Google Cloud Project**: Enabled with Vertex AI API.
## Setup
### 1. Backend (Python)
Navigate to the `backend` directory:
```bash
cd backend
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Set your Google Cloud Project ID and Location. You can copy `.env.example` to `.env` and fill in the details:
```bash
cp .env.example .env
# Edit .env with your details
```
Or export them directly:
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

Run the server:
```bash
python main.py
```
The server will start at `http://0.0.0.0:8080`.

#### Using Docker
Ensure you are in the `backend` directory:
```bash
cd backend
```

You can also run the backend using Docker:

```bash
docker build -t abu-dhabi-agent-backend .
docker run -p 8080:8080 -e GOOGLE_CLOUD_PROJECT="your-project-id" -e GOOGLE_CLOUD_LOCATION="us-central1" abu-dhabi-agent-backend
```
### 2. Mobile App (Flutter)
Navigate to the `mobile_app` directory:
```bash
cd mobile_app
```
Get dependencies:
```bash
flutter pub get
```
Run the app:
```bash
flutter run
```
**Note for Android Emulator**: The backend URL in `lib/chat_screen.dart` is set to `http://10.0.2.2:8080/chat` which is the special alias to your host machine's localhost. If running on a real device, change this to your computer's local IP address.
