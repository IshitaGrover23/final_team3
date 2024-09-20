document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('start-speech');
    const symptomInput = document.getElementById('id_symptoms');

    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            symptomInput.value += (symptomInput.value ? ', ' : '') + transcript;
        };

        startButton.addEventListener('click', function() {
            recognition.start();
        });
    } else {
        startButton.style.display = 'none';
        console.log('Speech recognition not supported');
    }
});