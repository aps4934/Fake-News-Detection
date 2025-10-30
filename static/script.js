document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');
    const loadingDiv = document.getElementById('loading');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const headline = document.getElementById('news').value.trim();
        if (!headline) {
            alert('Please enter a news headline');
            return;
        }

        // Show loading
        loadingDiv.style.display = 'block';
        resultDiv.style.display = 'none';

        // Call API
        fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: headline })
        })
        .then(response => response.json())
        .then(data => {
            loadingDiv.style.display = 'none';

            if (data.prediction && data.confidence) {
                const resultClass = data.prediction === 'REAL' ? 'real' : 'fake';
                const resultText = `Prediction: <span class="${resultClass}">${data.prediction}</span> (Confidence: ${data.confidence})`;
                resultDiv.innerHTML = `<h3>Analysis Result:</h3><p class="result-text">${resultText}</p>`;
                resultDiv.style.display = 'block';
            } else {
                resultDiv.innerHTML = '<h3>Error:</h3><p class="result-text">Unable to analyze the headline. Please try again.</p>';
                resultDiv.style.display = 'block';
            }
        })
        .catch(error => {
            loadingDiv.style.display = 'none';
            resultDiv.innerHTML = '<h3>Error:</h3><p class="result-text">Network error. Please try again.</p>';
            resultDiv.style.display = 'block';
            console.error('Error:', error);
        });
    });
});
