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

1. L'audio est d'abord transcrit en utilisant le modèle Whisper.
2. La transcription est ensuite envoyée au modèle BART pour générer un résumé.
3. Le résumé est généré avec une longueur adaptative, variant entre 30% et 50% de la longueur du texte original, avec un minimum de 30 mots et un maximum de 130 mots.
4. Les résultats (transcription et résumé) sont affichés sur la page web et sauvegardés localement.

## Dépannage

Si vous rencontrez des problèmes, en particulier avec le bouton "Commencer l'enregistrement", suivez ces étapes :

1. Assurez-vous d'utiliser un navigateur web moderne et à jour (Chrome, Firefox, ou Safari récent).

2. Vérifiez que le microphone est correctement connecté et reconnu par le système :
   - Utilisez la commande `arecord -l` pour lister les périphériques audio disponibles.

3. Ouvrez la console de développeur de votre navigateur (généralement F12 ou Ctrl+Shift+I) :
   - Vérifiez s'il y a des erreurs JavaScript affichées en rouge.
   - Recherchez les messages de log ajoutés pour le débogage, comme "Script chargé" ou "DOM entièrement chargé et analysé".

4. Si vous voyez une erreur indiquant que MediaRecorder n'est pas supporté, votre navigateur peut ne pas prendre en charge cette fonctionnalité. Essayez avec un navigateur différent.

5. Assurez-vous que vous avez accordé les permissions d'accès au microphone à votre navigateur lorsque demandé.

6. Si le problème persiste, essayez de redémarrer le serveur Flask et de recharger la page web.

7. En cas d'erreurs lors de l'exécution de l'application, vérifiez les logs dans la console où vous avez lancé `python app.py`.

## Remarques

- Le traitement peut prendre un certain temps en fonction de la longueur de l'audio et des performances de votre Raspberry Pi 5.
- L'utilisation de BART pour le résumé nécessite une quantité significative de mémoire et de puissance de calcul. Les performances peuvent varier en fonction de la configuration de votre Raspberry Pi 5.
- La longueur du résumé est automatiquement ajustée en fonction de la longueur de la transcription, ce qui permet d'obtenir des résumés plus pertinents et concis.
- Assurez-vous d'avoir suffisamment d'espace disque libre pour stocker les fichiers audio, les transcriptions et les modèles de langage.

Pour toute question ou problème persistant, n'hésitez pas à ouvrir une issue sur le dépôt GitHub du projet.