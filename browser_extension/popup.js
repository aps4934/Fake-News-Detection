// Popup script for Fake News Detector extension

const API_BASE_URL = 'http://127.0.0.1:5000'; // Change this for production

document.addEventListener('DOMContentLoaded', function() {
  // Check API connection
  checkConnection();

  // Load settings
  loadSettings();

  // Load history
  loadHistory();

  // Setup event listeners
  document.getElementById('analyze-btn').addEventListener('click', analyzeHeadline);
  document.getElementById('auto-scan').addEventListener('change', saveSettings);
  document.getElementById('show-confidence').addEventListener('change', saveSettings);
});

async function checkConnection() {
  const statusDiv = document.getElementById('status');

  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (response.ok) {
      statusDiv.textContent = '✅ Connected to API';
      statusDiv.className = 'status connected';
    } else {
      throw new Error('API not responding');
    }
  } catch (error) {
    statusDiv.textContent = '❌ Cannot connect to API';
    statusDiv.className = 'status disconnected';
    console.error('Connection check failed:', error);
  }
}

async function analyzeHeadline() {
  const headline = document.getElementById('headline').value.trim();
  const analyzeBtn = document.getElementById('analyze-btn');
  const resultDiv = document.getElementById('result');

  if (!headline) {
    showResult('Please enter a headline to analyze', 'error');
    return;
  }

  // Disable button and show loading
  analyzeBtn.disabled = true;
  analyzeBtn.textContent = 'Analyzing...';
  resultDiv.style.display = 'none';

  try {
    const response = await fetch(`${API_BASE_URL}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: headline })
    });

    const data = await response.json();

    if (data.prediction) {
      const isReal = data.prediction === 'REAL';
      const confidence = data.confidence || 'High';

      resultDiv.className = `result ${isReal ? 'real' : 'fake'}`;
      resultDiv.innerHTML = `
        <strong>Prediction: ${data.prediction}</strong><br>
        ${document.getElementById('show-confidence').checked ? `Confidence: ${confidence}` : ''}
      `;
      resultDiv.style.display = 'block';

      // Save to history
      saveToHistory(headline, data.prediction, confidence);
    } else {
      showResult('Error analyzing headline', 'error');
    }
  } catch (error) {
    console.error('Analysis failed:', error);
    showResult('Failed to analyze headline. Check your connection.', 'error');
  } finally {
    // Re-enable button
    analyzeBtn.disabled = false;
    analyzeBtn.textContent = '🔍 Analyze Headline';
  }
}

function showResult(message, type) {
  const resultDiv = document.getElementById('result');
  resultDiv.className = `result ${type}`;
  resultDiv.textContent = message;
  resultDiv.style.display = 'block';
}

function saveToHistory(text, prediction, confidence) {
  const history = JSON.parse(localStorage.getItem('fnd_history') || '[]');

  history.unshift({
    text: text.substring(0, 100), // Limit text length
    prediction: prediction,
    confidence: confidence,
    timestamp: new Date().toISOString()
  });

  // Keep only last 10 items
  if (history.length > 10) {
    history.splice(10);
  }

  localStorage.setItem('fnd_history', JSON.stringify(history));
  loadHistory();
}

function loadHistory() {
  const history = JSON.parse(localStorage.getItem('fnd_history') || '[]');
  const historyList = document.getElementById('history-list');

  if (history.length === 0) {
    historyList.innerHTML = '<div class="history-item">No analysis history yet</div>';
    return;
  }

  historyList.innerHTML = history.map(item => `
    <div class="history-item">
      <div class="text">${item.text}${item.text.length > 100 ? '...' : ''}</div>
      <div class="prediction ${item.prediction.toLowerCase()}">
        ${item.prediction} ${document.getElementById('show-confidence')?.checked ? `(${item.confidence})` : ''}
      </div>
    </div>
  `).join('');
}

function loadSettings() {
  const autoScan = localStorage.getItem('fnd_auto_scan') !== 'false'; // Default true
  const showConfidence = localStorage.getItem('fnd_show_confidence') === 'true'; // Default false

  document.getElementById('auto-scan').checked = autoScan;
  document.getElementById('show-confidence').checked = showConfidence;
}

function saveSettings() {
  const autoScan = document.getElementById('auto-scan').checked;
  const showConfidence = document.getElementById('show-confidence').checked;

  localStorage.setItem('fnd_auto_scan', autoScan);
  localStorage.setItem('fnd_show_confidence', showConfidence);

  // Notify content script of settings change
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    if (tabs[0]) {
      chrome.tabs.sendMessage(tabs[0].id, {
        action: 'settingsChanged',
        settings: { autoScan, showConfidence }
      });
    }
  });
}

// Context menu integration
chrome.contextMenus.create({
  title: "Analyze with Fake News Detector",
  contexts: ["selection"],
  onclick: function(info, tab) {
    const selectedText = info.selectionText;
    if (selectedText) {
      // Open popup with selected text
      chrome.browserAction.openPopup();
      // This is a simplified approach - in practice, you'd need to pass the text to the popup
    }
  }
});
