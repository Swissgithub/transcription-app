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

# Tenter d'installer tiktoken séparément
pip uninstall -y tiktoken
pip install --no-binary :all: tiktoken==0.1.2

# Installer Whisper et ses dépendances
pip install git+https://github.com/openai/whisper.git 

# Télécharger le modèle LLaMA
python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; AutoTokenizer.from_pretrained('meta-llama/Llama-2-7b-chat-hf'); AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-chat-hf')"

echo "Installation terminée. Activez l'environnement virtuel avec 'source venv/bin/activate' avant de lancer l'application. Les modèles Whisper et LLaMA ont été téléchargés."

# Vérifier l'installation de tiktoken
python -c "import tiktoken; print('Tiktoken installé avec succès')" || echo "Erreur lors de l'importation de tiktoken"