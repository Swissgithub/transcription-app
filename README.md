# Application de Transcription et Résumé pour Raspberry Pi 5

Cette application permet de transcrire des fichiers audio ou vidéo, ainsi que d'enregistrer et de transcrire l'audio à partir du microphone. Elle utilise Whisper pour la transcription et le modèle LLaMA pour générer un résumé de la transcription.

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

   Ce script installera toutes les dépendances nécessaires, configurera l'environnement et téléchargera les modèles Whisper et LLaMA.

### Note importante sur l'installation

Si vous rencontrez des problèmes lors de l'installation, en particulier avec la bibliothèque tiktoken, le script d'installation tentera de la compiler à partir des sources. Cela peut prendre un certain temps, soyez patient.

En cas d'échec de l'installation, vous pouvez essayer les étapes suivantes manuellement :

1. Activez l'environnement virtuel :
   ```
   source venv/bin/activate
   ```

2. Mettez à jour pip et les outils de build :
   ```
   pip install --upgrade pip setuptools wheel
   ```

3. Installez tiktoken à partir des sources :
   ```
   pip install --no-binary :all: tiktoken
   ```

4. Réinstallez les autres dépendances :
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Assurez-vous que votre microphone USB est correctement connecté et reconnu par le système.

2. Si nécessaire, ajustez les paramètres du microphone dans le fichier `app.py`.

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

1. L'audio est transcrit en utilisant le modèle Whisper "medium".
2. Une fois la transcription terminée, le modèle Whisper est déchargé de la mémoire.
3. La transcription est ensuite envoyée au modèle LLaMA pour générer un résumé.
4. LLaMA génère un résumé dans la même langue que la transcription.
5. Après la génération du résumé, le modèle LLaMA est déchargé de la mémoire.
6. Les résultats (transcription et résumé) sont affichés sur la page web et sauvegardés localement.

## Remarques importantes

- Les modèles sont chargés et déchargés séquentiellement pour optimiser l'utilisation de la mémoire.
- Le traitement peut prendre un certain temps, en particulier pour les fichiers audio longs.
- L'utilisation de Whisper "medium" et de LLaMA nécessite une quantité significative de mémoire et de puissance de calcul. Les performances peuvent varier en fonction de la configuration de votre Raspberry Pi 5.
- La transcription est capable de gérer des fichiers audio de toutes longueurs.
- Le résumé est généré dans la même langue que la transcription originale.

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez les logs de l'application dans la console où vous avez lancé `python app.py` pour des informations de débogage sur le processus de transcription et de résumé.

2. Assurez-vous que votre Raspberry Pi 5 dispose de suffisamment de ressources (mémoire et CPU) pour exécuter les modèles de transcription et de résumé.

3. Pour les problèmes liés au bouton "Commencer l'enregistrement", consultez la console de développeur de votre navigateur (F12 ou Ctrl+Shift+I) pour voir les messages de log et les erreurs potentielles.

4. Si la transcription ou le résumé échouent pour des fichiers spécifiques, assurez-vous qu'ils sont dans un format audio supporté (WAV, MP3, etc.).

5. En cas de problèmes persistants avec tiktoken ou d'autres dépendances, essayez de les réinstaller manuellement comme décrit dans la section "Note importante sur l'installation".

Pour toute question ou problème persistant, n'hésitez pas à ouvrir une issue sur le dépôt GitHub du projet.