// Content script for Fake News Detector extension

let settings = {
  autoScan: true,
  showConfidence: false
};

// Load settings from storage
chrome.storage.local.get(['fnd_auto_scan', 'fnd_show_confidence'], function(result) {
  settings.autoScan = result.fnd_auto_scan !== false; // Default true
  settings.showConfidence = result.fnd_show_confidence === true; // Default false

  if (settings.autoScan) {
    scanHeadlines();
  }
});

// Listen for settings changes
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'settingsChanged') {
    settings = request.settings;
    if (settings.autoScan) {
      scanHeadlines();
    } else {
      removeHighlights();
    }
  }
});

function scanHeadlines() {
  // Common selectors for news headlines
  const selectors = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    '.headline', '.title', '.news-title',
    '[class*="headline"]', '[class*="title"]',
    'article h1', 'article h2', 'article .title',
    '.post-title', '.entry-title',
    '.article-title', '.story-title'
  ];

  selectors.forEach(selector => {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
      if (!element.hasAttribute('data-fnd-processed')) {
        analyzeElement(element);
      }
    });
  });
}

async function analyzeElement(element) {
  const text = element.textContent.trim();
  if (text.length < 10 || text.length > 200) return; // Skip very short or very long text

  element.setAttribute('data-fnd-processed', 'true');

  try {
    const response = await fetch('http://127.0.0.1:5000/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    if (data.prediction) {
      highlightElement(element, data.prediction, data.confidence);
    }
  } catch (error) {
    console.log('Failed to analyze element:', error);
  }
}

function highlightElement(element, prediction, confidence) {
  const isReal = prediction === 'REAL';

  // Create highlight overlay
  const overlay = document.createElement('div');
  overlay.className = 'fnd-highlight-overlay';
  overlay.style.cssText = `
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: ${isReal ? 'rgba(76, 175, 80, 0.1)' : 'rgba(244, 67, 54, 0.1)'};
    border: 2px solid ${isReal ? '#4CAF50' : '#f44336'};
    border-radius: 4px;
    pointer-events: none;
    z-index: 9999;
  `;

  // Make element position relative if not already
  const computedStyle = window.getComputedStyle(element);
  if (computedStyle.position === 'static') {
    element.style.position = 'relative';
  }

  element.style.borderRadius = '4px';

  // Add tooltip
  const tooltip = document.createElement('div');
  tooltip.className = 'fnd-tooltip';
  tooltip.textContent = `${prediction}${settings.showConfidence && confidence ? ` (${confidence})` : ''}`;
  tooltip.style.cssText = `
    position: absolute;
    top: -30px;
    left: 0;
    background-color: ${isReal ? '#4CAF50' : '#f44336'};
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
    white-space: nowrap;
    z-index: 10000;
    opacity: 0;
    transition: opacity 0.3s ease;
  `;

  overlay.appendChild(tooltip);
  element.appendChild(overlay);

  // Show tooltip on hover
  element.addEventListener('mouseenter', () => {
    tooltip.style.opacity = '1';
  });

  element.addEventListener('mouseleave', () => {
    tooltip.style.opacity = '0';
  });
}

function removeHighlights() {
  const overlays = document.querySelectorAll('.fnd-highlight-overlay');
  overlays.forEach(overlay => overlay.remove());
}

// Add styles for highlights
const style = document.createElement('style');
style.textContent = `
  .fnd-highlight-overlay {
    transition: all 0.3s ease;
  }

  .fnd-tooltip {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }

  .fnd-tooltip::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 10px;
    border: 5px solid transparent;
    border-top-color: currentColor;
  }
`;
document.head.appendChild(style);

// Re-scan when new content is loaded (for dynamic pages)
const observer = new MutationObserver(function(mutations) {
  if (settings.autoScan) {
    mutations.forEach(function(mutation) {
      if (mutation.type === 'childList') {
        mutation.addedNodes.forEach(function(node) {
          if (node.nodeType === Node.ELEMENT_NODE) {
            scanHeadlines();
          }
        });
      }
    });
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true
});

// Handle right-click context menu
document.addEventListener('contextmenu', function(event) {
  const selectedText = window.getSelection().toString().trim();
  if (selectedText) {
    chrome.runtime.sendMessage({
      action: 'analyzeSelection',
      text: selectedText
    });
  }
});
