# Application de Transcription et Résumé pour Raspberry Pi 5

Cette application permet de transcrire des fichiers audio ou vidéo, ainsi que d'enregistrer et de transcrire l'audio à partir du microphone. Elle utilise Whisper pour la transcription et le modèle BART pour générer un résumé de la transcription.

## Prérequis

- Raspberry Pi 5 avec au moins 8 Go de RAM
- Au moins 10 Go d'espace de stockage libre
- Microphone USB connecté à la carte 2 / device 0
- Système d'exploitation Raspberry Pi OS (64-bit) installé et à jour
- Navigateur web moderne (Chrome, Firefox, ou Safari récent)

## Installation

1. Clonez ce dépôt sur votre Raspberry Pi 5 :
   ```
   git clone https://github.com/votre-nom/transcription-app.git
   cd transcription-app
   ```

2. Rendez le script d'installation exécutable :
   ```
   chmod +x install.sh
   ```

3. Exécutez le script d'installation :
   ```
   ./install.sh
   ```

   Ce script installera toutes les dépendances nécessaires, configurera l'environnement et téléchargera les modèles Whisper et BART.

## Configuration

1. Assurez-vous que votre microphone USB est correctement connecté et reconnu par le système.

2. Si nécessaire, ajustez les paramètres du microphone dans le fichier `app.py` :
   ```python
   # Dans la fonction record_audio()
   device_index = 0  # Modifiez cette valeur si nécessaire
   ```

## Exécution de l'application

1. Activez l'environnement virtuel :
   ```
   source venv/bin/activate
   ```

2. Lancez l'application :
   ```
   python app.py
   ```

3. Ouvrez un navigateur web et accédez à `http://localhost:5000` (ou l'adresse IP de votre Raspberry Pi si vous y accédez depuis un autre appareil sur le réseau local).

## Utilisation

1. Pour transcrire un fichier audio ou vidéo :
   - Cliquez sur "Choisir un fichier" et sélectionnez le fichier à transcrire.
   - Cliquez sur "Télécharger" pour lancer la transcription et le résumé.

2. Pour enregistrer et transcrire à partir du microphone :
   - Cliquez sur "Commencer l'enregistrement".
   - Parlez dans le microphone.
   - Cliquez sur "Arrêter l'enregistrement" lorsque vous avez terminé.

3. La transcription et le résumé s'afficheront automatiquement une fois le traitement terminé.

## Fonctionnement

1. L'audio est transcrit en utilisant le modèle Whisper "medium" pour une meilleure qualité.
2. La transcription est ensuite envoyée au modèle BART pour générer un résumé.
3. Le résumé est généré avec une longueur adaptative, variant entre 30% et 50% de la longueur du texte original, avec un minimum de 30 mots et un maximum de 130 mots.
4. Les résultats (transcription et résumé) sont affichés sur la page web et sauvegardés localement.

## Remarques importantes

- Le traitement peut prendre un certain temps, en particulier pour les fichiers audio longs, en raison de l'utilisation du modèle Whisper "medium".
- L'utilisation du modèle Whisper "medium" et de BART pour le résumé nécessite une quantité significative de mémoire et de puissance de calcul. Les performances peuvent varier en fonction de la configuration de votre Raspberry Pi 5.
- La transcription est maintenant capable de gérer des fichiers audio de toutes longueurs, résolvant le problème précédent de transcriptions incomplètes.
- Assurez-vous d'avoir suffisamment d'espace disque libre pour stocker les fichiers audio, les transcriptions et les modèles de langage.

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez les logs de l'application dans la console où vous avez lancé `python app.py` pour des informations de débogage sur le processus de transcription.

2. Assurez-vous que votre Raspberry Pi 5 dispose de suffisamment de ressources (mémoire et CPU) pour exécuter les modèles de transcription et de résumé.

3. Pour les problèmes liés au bouton "Commencer l'enregistrement", consultez la console de développeur de votre navigateur (F12 ou Ctrl+Shift+I) pour voir les messages de log et les erreurs potentielles.

4. Si la transcription échoue pour des fichiers spécifiques, assurez-vous qu'ils sont dans un format audio supporté (WAV, MP3, etc.).

Pour toute question ou problème persistant, n'hésitez pas à ouvrir une issue sur le dépôt GitHub du projet.