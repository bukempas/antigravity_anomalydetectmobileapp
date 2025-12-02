# Agentic Mobile App (Flutter + Python ADK)
This project demonstrates a mobile app that uses a Python backend powered by Google's Agent Development Kit (ADK) / Vertex AI to answer questions about Abu Dhabi and GovAI.
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
Set your Google Cloud Project ID and Location (if not using default):
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```
Run the server:
```bash
python main.py
```
The server will start at `http://0.0.0.0:8080`.
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
