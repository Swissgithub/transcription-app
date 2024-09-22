console.log("Script chargé");

let mediaRecorder;
let audioChunks = [];

// Vérifier si le navigateur supporte MediaRecorder
if (!window.MediaRecorder) {
    console.error("MediaRecorder n'est pas supporté par ce navigateur");
    alert("Votre navigateur ne supporte pas l'enregistrement audio. Veuillez utiliser un navigateur moderne comme Chrome ou Firefox.");
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Veuillez sélectionner un fichier');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    updateStatus('Téléchargement du fichier...');
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        transcribeAudio(data.filename);
    })
    .catch(error => {
        console.error('Error:', error);
        updateStatus('Erreur lors du téléchargement du fichier');
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    console.log("DOM entièrement chargé et analysé");
    const recordButton = document.getElementById('recordButton');
    if (recordButton) {
        recordButton.addEventListener('click', toggleRecording);
        console.log("Event listener ajouté au bouton d'enregistrement");
    } else {
        console.error("Bouton d'enregistrement non trouvé");
    }
});

function toggleRecording() {
    console.log("Fonction toggleRecording appelée");
    if (mediaRecorder && mediaRecorder.state === "recording") {
        stopRecording();
    } else {
        startRecording();
    }
}

function startRecording() {
    console.log("Démarrage de l'enregistrement");
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
            mediaRecorder.onstop = sendAudioData;
            mediaRecorder.start();
            updateStatus('Enregistrement en cours...');
            document.getElementById('recordButton').textContent = 'Arrêter l\'enregistrement';
        })
        .catch(error => {
            console.error('Error accessing microphone:', error);
            updateStatus('Erreur d\'accès au microphone');
        });
}

function stopRecording() {
    console.log("Arrêt de l'enregistrement");
    if (mediaRecorder) {
        mediaRecorder.stop();
        updateStatus('Traitement de l\'enregistrement...');
        document.getElementById('recordButton').textContent = 'Commencer l\'enregistrement';
    }
}

function sendAudioData() {
    console.log("Envoi des données audio");
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('audio', audioBlob, 'recording.wav');

    fetch('/record', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        transcribeAudio(data.filename);
    })
    .catch(error => {
        console.error('Error:', error);
        updateStatus('Erreur lors de l\'envoi de l\'audio');
    });

    audioChunks = [];
}

function transcribeAudio(filename) {
    updateStatus('Transcription en cours...');
    fetch('/transcribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filename: filename })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('transcription').textContent = data.transcription;
        document.getElementById('summary').textContent = data.summary;
        updateStatus('Transcription et résumé terminés');
    })
    .catch(error => {
        console.error('Error:', error);
        updateStatus('Erreur lors de la transcription');
    });
}

function updateStatus(message) {
    const statusElement = document.getElementById('status');
    statusElement.textContent = message;
}