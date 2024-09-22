#!/bin/bash

# Mettre à jour le système
sudo apt update
sudo apt upgrade -y

# Installer les dépendances système
sudo apt install -y python3-pip python3-venv portaudio19-dev ffmpeg

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances Python
pip install -r requirements.txt

# Installer Whisper et ses dépendances
pip install git+https://github.com/openai/whisper.git 
sudo apt install -y ffmpeg

# Télécharger le modèle BART
python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; AutoTokenizer.from_pretrained('facebook/bart-large-cnn'); AutoModelForSeq2SeqLM.from_pretrained('facebook/bart-large-cnn')"

echo "Installation terminée. Activez l'environnement virtuel avec 'source venv/bin/activate' avant de lancer l'application. Les modèles Whisper et BART ont été téléchargés."