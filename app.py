from flask import Flask, render_template, request, jsonify
import os
import whisper
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

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
    
    print(f"Transcribing file: {file_path}")  # Log pour le débogage
    
    # Charger le modèle Whisper
    whisper_model = whisper.load_model("medium")
    
    try:
        # Transcrire l'audio
        result = whisper_model.transcribe(file_path, fp16=False)
        transcription = result["text"]
        
        print(f"Transcription completed. Length: {len(transcription)} characters")  # Log pour le débogage
        
        # Sauvegarder la transcription
        transcription_filename = os.path.join(TRANSCRIPTION_FOLDER, f"{os.path.splitext(filename)[0]}_transcription.txt")
        with open(transcription_filename, 'w') as f:
            f.write(transcription)
        
        # Libérer la mémoire du modèle Whisper
        del whisper_model
        torch.cuda.empty_cache()
        
        # Générer le résumé
        summary = summarize(transcription)
        
        return jsonify({"transcription": transcription, "summary": summary, "filename": transcription_filename})
    
    except Exception as e:
        print(f"Error during transcription: {str(e)}")  # Log pour le débogage
        return jsonify({"error": "Transcription failed"}), 500

def summarize(text):
    print("Starting summarization")  # Log pour le débogage
    
    # Charger le modèle LLaMA
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    
    prompt = f"summarize me the following transcription. The summarization must be in the same language as the transcription: {text}"
    
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Générer le résumé
    with torch.no_grad():
        output = model.generate(**inputs, max_length=150, num_return_sequences=1)
    
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Libérer la mémoire du modèle LLaMA
    del model
    del tokenizer
    torch.cuda.empty_cache()
    
    print("Summarization completed")  # Log pour le débogage
    
    return summary

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)