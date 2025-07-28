# 🧠 AI Voice Assistant

A voice-based assistant that transcribes your speech, sends it to an AI for response, and speaks the reply back—all in one flow. This project uses:

- 🎙️ [Whisper](https://github.com/openai/whisper) for speech-to-text
- 🤖 [OpenRouter](https://openrouter.ai) (ChatGPT-like models) for response generation
- 🔊 [gTTS](https://pypi.org/project/gTTS/) for text-to-speech
- 🌐 Flask backend with CORS support

---

## 🚀 Features

- Record voice directly from browser
- Transcribe using Whisper (multilingual support)
- AI-generated responses via OpenRouter
- Human-like audio reply using gTTS
- Return both text and audio to the user

---

## 📁 Project Structure

AIVoiceAssistant/
├── static/
│ └── reply_audio.mp3 # Generated audio
├── templates/
│ └── index.html # Frontend UI
├── audios/ # Temporary storage for user recordings
├── app.py # Flask backend logic
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy
Edit

---

## 🧠 Requirements

- Python 3.9 or 3.10 (recommended)
- FFmpeg (required by Whisper and audio conversion)

---

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AIVoiceAssistant.git
cd AIVoiceAssistant
```
2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install flask flask-cors openai-whisper gtts requests
```
4. Install FFmpeg

Windows: https://ffmpeg.org/download.html → Add to PATH

Linux: sudo apt install ffmpeg

Mac: brew install ffmpeg

🔑 Configure API
In app.py, replace this with your OpenRouter API Key:

api_key = "sk-or-..."
▶️ Run the App
```bash
python app.py
```
Visit: http://127.0.0.1:5000

Speak, release the mic, and get a spoken AI reply!

Use Python 3.9 or 3.10. Python 3.11+ is incompatible with Whisper.

🧠 Use Cases
Government scheme Q&A bots
Voice interfaces for visually impaired
Multilingual support agents
Language learning assistant

🙌 Credits
OpenAI Whisper
gTTS
OpenRouter
Flask + HTML/JS frontend

📬 Feedback
Pull requests and ideas welcome!

