# Fake News Detector Browser Extension

A browser extension that automatically detects fake news headlines using AI-powered analysis.

## Features

- **Automatic Detection**: Scans news headlines on websites and highlights them based on authenticity
- **Manual Analysis**: Right-click on any text to analyze it instantly
- **Popup Interface**: Quick access to analyze headlines via the extension popup
- **Visual Indicators**: Color-coded highlights (green for real news, red for fake news)
- **Privacy First**: All analysis is done locally, no data is sent to external servers
- **Customizable Settings**: Configure auto-scanning and confidence score display

## Installation

### For Development/Testing

1. **Clone or download** the extension files from the `browser_extension/` directory
2. **Open your browser's extension page**:
   - Chrome: `chrome://extensions/`
   - Firefox: `about:addons`
   - Edge: `edge://extensions/`
3. **Enable Developer Mode** (usually a toggle in the top-right corner)
4. **Click "Load unpacked"** and select the `browser_extension/` folder
5. **The extension should now be installed** and visible in your browser toolbar

### For Production

1. **Package the extension**:
   - Create a ZIP file containing all files in the `browser_extension/` directory
   - Remove any development files (like this README)
2. **Submit to browser stores**:
   - Chrome Web Store
   - Firefox Add-ons
   - Microsoft Edge Add-ons

## Usage

### Automatic Scanning
- The extension automatically scans for headlines on news websites
- Headlines are highlighted with colored borders and tooltips
- Green highlights indicate real news
- Red highlights indicate fake news

### Manual Analysis
- **Right-click** on any selected text and choose "Analyze with Fake News Detector"
- **Use the extension popup** by clicking the extension icon and entering text

### Settings
- **Auto-scan headlines**: Enable/disable automatic scanning on web pages
- **Show confidence scores**: Display confidence levels in tooltips and results

## API Integration

The extension communicates with the Fake News Detector Flask API running on `http://127.0.0.1:5000`. Make sure the Flask app is running before using the extension.

### Required API Endpoints

- `POST /api/predict`: Analyze text for fake news
  ```json
  {
    "text": "News headline to analyze"
  }
  ```

- `GET /health`: Check API availability

## File Structure

```
browser_extension/
├── manifest.json          # Extension manifest
├── popup.html            # Extension popup interface
├── popup.js              # Popup functionality
├── content.js            # Content script for web page analysis
├── background.js         # Background service worker
├── styles.css            # Content script styles
└── README.md             # This file
```

## Browser Compatibility

- **Chrome**: Version 88+
- **Firefox**: Version 78+
- **Microsoft Edge**: Version 88+
- **Other Chromium browsers**: Should work with manifest v3 support

## Permissions

The extension requires the following permissions:

- `activeTab`: Access the current active tab
- `contextMenus`: Create right-click context menus
- `storage`: Store user settings and analysis history
- `http://*/` and `https://*/`: Access web pages for content analysis

## Development

### Testing the Extension

1. **Load the unpacked extension** in your browser
2. **Start the Flask API** on `http://127.0.0.1:5000`
3. **Visit news websites** to test automatic scanning
4. **Use the popup** to test manual analysis
5. **Check browser console** for debugging information

### Modifying the Extension

- **manifest.json**: Update extension metadata and permissions
- **popup.html/popup.js**: Modify the popup interface and functionality
- **content.js**: Change how web pages are analyzed
- **background.js**: Update background processes and context menus
- **styles.css**: Customize visual appearance

## Troubleshooting

### Extension Not Working

1. **Check API connection**: Ensure Flask app is running on port 5000
2. **Verify permissions**: Make sure all required permissions are granted
3. **Check console**: Look for errors in browser developer tools
4. **Reload extension**: Try reloading the extension in the extensions page

### Highlights Not Appearing

1. **Enable auto-scan**: Check that auto-scanning is enabled in settings
2. **Refresh page**: Reload the web page after enabling auto-scan
3. **Check selectors**: The extension may not detect all headline formats

### API Connection Issues

1. **Firewall**: Ensure port 5000 is not blocked
2. **CORS**: The Flask app should allow requests from browser extensions
3. **Network**: Check that the browser can reach localhost:5000

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the main project LICENSE file for details.

## Support

For support or questions:
- Create an issue on GitHub
- Check the main project documentation
- Contact the development team
