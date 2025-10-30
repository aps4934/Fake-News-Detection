// Background script for Fake News Detector extension

// Handle extension installation
chrome.runtime.onInstalled.addListener(function() {
  console.log('Fake News Detector extension installed');

  // Create context menu
  chrome.contextMenus.create({
    title: "Analyze with Fake News Detector",
    contexts: ["selection"],
    id: "analyze-selection"
  });

  // Set default settings
  chrome.storage.local.set({
    'fnd_auto_scan': true,
    'fnd_show_confidence': false
  });
});

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener(function(info, tab) {
  if (info.menuItemId === "analyze-selection" && info.selectionText) {
    // Store selected text for popup
    chrome.storage.local.set({
      'selected_text': info.selectionText
    });

    // Open popup
    chrome.action.openPopup();
  }
});

// Handle messages from popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'analyzeSelection') {
    // This would be handled by the popup opening with the selected text
    sendResponse({success: true});
  }
});

// Handle extension icon click (if no popup is set)
chrome.action.onClicked.addListener(function(tab) {
  // This is a fallback if popup doesn't work
  chrome.tabs.create({url: chrome.runtime.getURL('popup.html')});
});
