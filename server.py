from flask import Flask, request, jsonify, send_file
import os
import tempfile
import subprocess
import whisper
import requests
from gtts import gTTS
from flask_cors import CORS

# Load Whisper model once
model = whisper.load_model("small")

app = Flask(__name__)
CORS(app)  


@app.route('/process', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio uploaded"}), 400

    audio_file = request.files['audio']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_input:
        audio_file.save(temp_input.name)
        input_path = temp_input.name

    # Convert WebM to WAV
    wav_path = input_path.replace(".webm", ".wav")
    subprocess.run(["ffmpeg", "-i", input_path, wav_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Transcribe
    result = model.transcribe(wav_path)
    transcript = result['text']

    # Get AI reply
    lang = 'hi'
    reply_text = get_humanlike_reply(transcript, lang)

    # TTS
    reply_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts = gTTS(text=reply_text, lang=lang)
    tts.save(reply_audio.name)

    return jsonify({
        "transcript": transcript,
        "reply_text": reply_text,
        "reply_audio_url": f"/audio/{os.path.basename(reply_audio.name)}"
    })


@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_file(os.path.join(tempfile.gettempdir(), filename), mimetype="audio/mpeg")

def get_humanlike_reply(message, lang="hi"):
    api_key = "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"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    system_prompt = f"""
You are a kind, multilingual AI assistant who helps Indian citizens understand and access government schemes and social services.
Always respond like a human: natural, helpful, empathetic, and friendly.
Always respond in native script of the language (Hindi = देवनागरी, Bengali = বাংলা, Tamil = தமிழ்).
Also ask a polite follow-up if more info is needed.

Language: {lang}
"""

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
