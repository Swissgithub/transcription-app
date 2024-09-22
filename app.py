from flask import Flask, render_template, request, jsonify
import os
import whisper
import torch
from transformers import pipeline
import soundfile as sf
from pydub import AudioSegment

app = Flask(__name__)

# Charger les modèles
whisper_model = whisper.load_model("medium")  # Utilisation du modèle "medium" pour une meilleure qualité

# Initialiser le modèle de résumé BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

UPLOAD_FOLDER = 'uploads'
TRANSCRIPTION_FOLDER = 'transcriptions'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(TRANSCRIPTION_FOLDER):
    os.makedirs(TRANSCRIPTION_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        return jsonify({"message": "File uploaded successfully", "filename": file.filename})

@app.route('/record', methods=['POST'])
def record_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio data"}), 400
    audio_file = request.files['audio']
    if audio_file:
        filename = os.path.join(UPLOAD_FOLDER, "recorded_audio.wav")
        audio_file.save(filename)
        return jsonify({"message": "Audio recorded successfully", "filename": "recorded_audio.wav"})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    filename = request.json.get('filename')
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Convertir en format WAV si nécessaire
    if not filename.lower().endswith('.wav'):
        audio = AudioSegment.from_file(file_path)
        file_path = os.path.join(UPLOAD_FOLDER, f"{os.path.splitext(filename)[0]}.wav")
        audio.export(file_path, format="wav")
    
    print(f"Transcribing file: {file_path}")  # Log pour le débogage
    
    # Charger et transcrire l'audio
    try:
        result = whisper_model.transcribe(file_path, fp16=False)
        transcription = result["text"]
    except Exception as e:
        print(f"Error during transcription: {str(e)}")  # Log pour le débogage
        return jsonify({"error": "Transcription failed"}), 500
    
    print(f"Transcription completed. Length: {len(transcription)} characters")  # Log pour le débogage
    
    # Sauvegarder la transcription
    transcription_filename = os.path.join(TRANSCRIPTION_FOLDER, f"{os.path.splitext(filename)[0]}_transcription.txt")
    with open(transcription_filename, 'w') as f:
        f.write(transcription)
    
    # Générer le résumé
    summary = summarize(transcription)
    
    return jsonify({"transcription": transcription, "summary": summary, "filename": transcription_filename})

def summarize(text):
    # Calculer la longueur du texte en mots
    word_count = len(text.split())
    
    # Calculer la longueur maximale du résumé (30% à 50% du texte original)
    max_length = max(30, min(int(word_count * 0.5), 130))
    min_length = max(30, min(int(word_count * 0.3), 100))
    
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
    return summary

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)