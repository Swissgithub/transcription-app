#!/bin/bash

# Mettre à jour le système
sudo apt update
sudo apt upgrade -y

# Installer les dépendances système
sudo apt install -y python3-pip python3-venv portaudio19-dev ffmpeg build-essential python3-dev

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Mettre à jour pip, setuptools et wheel
pip install --upgrade pip setuptools wheel

# Installer les dépendances Python
pip install -r requirements.txt

# Installer Whisper et ses dépendances
pip install git+https://github.com/openai/whisper.git 

# Installer tiktoken à partir des sources
pip install --no-binary :all: tiktoken

# Télécharger le modèle LLaMA
python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-chat-hf'); AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-chat-hf')"

echo "Installation terminée. Activez l'environnement virtuel avec 'source venv/bin/activate' avant de lancer l'application. Les modèles Whisper et LLaMA ont été téléchargés."