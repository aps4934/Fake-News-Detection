# Fake News Detection 📰🤖

[![Live Demo](https://img.shields.io/badge/Live%20Demo-View%20Project-blue)](https://fake-news-detection-1-vgdh.onrender.com)


A modern, professional web application built with Python Flask for detecting fake news using advanced machine learning models including BERT/Transformers. Features a beautiful, responsive UI, real-time news fetching, browser extension, and comprehensive documentation.

## 🚀 Features

- **🤖 Advanced AI Detection**: BERT/Transformers model for superior fake news detection with fallback system
- **📰 Real-time News Fetching**: Aggregate news from multiple online sources using NewsAPI
- **🌐 Browser Extension**: Chrome/Firefox extension for one-click fake news detection on any webpage
- **🎨 Modern Single-Page UI**: Responsive design with AJAX-powered predictions and improved visibility
- **📊 PDF Report Generation**: Generate professional PDF reports of analysis results
- **🧪 Comprehensive Testing**: Full test suite with 7/7 tests passing
- **📱 Mobile Responsive**: Works perfectly on all devices
- **⚡ Fast Processing**: Real-time predictions with sub-second response times
- **🗄️ Database Integration**: SQLite database for news storage and management

## ⚙️ Installation (Local Setup)

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Clone the repository

```bash
git clone https://github.com/aps4934/Fake-News-Detection.git
cd Fake-News-Detection
```

### Create a virtual environment (recommended)

```bash
python -m venv newsapp
source newsapp/bin/activate   # On Linux/Mac
newsapp\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set up environment variables (optional)

Create a `.env` file for NewsAPI key:
```bash
NEWS_API_KEY=your_newsapi_key_here
```

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

## 🔧 API Endpoints

### Main Routes
- `GET /` - Home page with prediction form and comprehensive information
- `GET /news` - View fetched news articles
- `GET /extension` - Browser extension information and download
- `GET /health` - Health check endpoint for monitoring

### API Endpoints
- `POST /api/predict` - Fake news detection API
  ```json
  {
    "text": "Your news headline here"
  }
  ```
- `GET /api/fetch_news` - Fetch latest news articles
- `POST /prediction` - Legacy prediction endpoint

### PDF Report Generation
```bash
curl -X POST http://localhost:5000/generate_report \
  -d "news=Your news headline here" \
  -o fake_news_report.pdf
```

## 🌐 Deployment on Render

### Step 1: Connect Your Repository
1. Go to [Render.com](https://render.com) and sign in
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository (`aps4934/Fake-News-Detection`)

### Step 2: Configure Build Settings
- **Name**: `fake-news-detection` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`

### Step 3: Add Environment Variables
In the Render dashboard, add these environment variables:
- `NEWS_API_KEY`: Your NewsAPI key (optional, for news fetching)
- `FLASK_ENV`: `production`

### Step 4: Deploy
- Click "Create Web Service"
- Render will automatically build and deploy your application
- Your app will be available at `https://your-app-name.onrender.com`

### Troubleshooting Render Deployment
- **Build Failures**: Check the build logs for specific error messages
- **Python Version**: Render uses Python 3.13.4 - ensure compatibility
- **Dependencies**: All packages in `requirements.txt` must be compatible with Python 3.13
- **Port**: Use `$PORT` environment variable for the port binding

## 🛠 Technology Stack

### Backend
- **Python Flask**: Web framework for the application
- **BERT/Transformers**: Advanced NLP model for fake news detection
- **Scikit-learn**: Traditional ML models with TF-IDF vectorization
- **NewsAPI**: Real-time news fetching and aggregation
- **SQLite**: Database for news storage
- **Gunicorn**: WSGI server for production deployment
- **WeasyPrint**: PDF generation for professional reports

### Frontend
- **HTML5**: Semantic markup structure
- **Custom CSS**: Modern styling with dark theme and animations
- **JavaScript**: AJAX functionality for seamless user experience
- **Responsive Design**: Mobile-first approach with breakpoints

### Machine Learning
- **BERT Model**: State-of-the-art transformer model for text classification
- **Fallback System**: Traditional ML models for reliability
- **TF-IDF Vectorization**: Feature extraction from text data
- **Cross-validation**: Ensures model reliability and accuracy
- **Real-time Processing**: Sub-second prediction times

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py                    # Main Flask application
├── app_new.py               # Alternative app configuration
├── requirements.txt         # Python dependencies
├── Procfile                # Heroku deployment configuration
├── test_app.py             # Comprehensive test suite
├── test_pdf.py             # PDF generation tests
├── TODO.md                 # Project roadmap and tasks
│
├── models/                 # Machine learning models
│   ├── bert_model.py       # BERT implementation
│   └── __pycache__/
│
├── utils/                  # Utility functions
│   ├── news_fetcher.py     # News API integration
│   └── __pycache__/
│
├── browser_extension/      # Browser extension files
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   ├── content.js
│   ├── background.js
│   ├── styles.css
│   └── README.md
│
├── templates/              # HTML templates
│   ├── index.html          # Main page with prediction form
│   ├── prediction.html     # Legacy prediction page
│   ├── news.html           # News articles display
│   ├── extension.html      # Extension information
│   └── headlines.html
│
├── static/                 # Static files
│   ├── styles.css          # Custom CSS styling
│   └── script.js           # JavaScript functionality
│
└── instance/               # Database files
    └── news_headlines.db
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_app.py
```

Expected output: `📊 Test Results: 7/7 tests passed`

## 🌐 Browser Extension Setup

### Chrome Extension
1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked" and select the `browser_extension` folder
4. The extension will be installed and ready to use

### Firefox Extension
1. Open Firefox and go to `about:debugging`
2. Click "This Firefox" → "Load Temporary Add-on"
3. Select `manifest.json` from the `browser_extension` folder

## 📊 Usage Examples

### API Usage
```python
import requests

# Test fake news detection
response = requests.post('http://localhost:5000/api/predict',
                        json={'text': 'Your news headline here'})
print(response.json())
# {'prediction': 'REAL', 'confidence': 'High', 'timestamp': '...'}

# Fetch news articles
news = requests.get('http://localhost:5000/api/fetch_news')
print(news.json())
```

### Browser Extension
1. Install the extension as described above
2. Navigate to any news website
3. Click the extension icon
4. Paste or select headline text
5. Get instant fake news analysis

## 👤 Creator

Created by Aditya Pratap Singh (aps4934).  
Email: sadityapratap070@gmail.com  
LinkedIn: https://www.linkedin.com/in/aps4934g/  
Portfolio: https://portfolio-3hns.onrender.com/  
GitHub: https://github.com/aps4934  

Feel free to open issues or submit pull requests for improvements!

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- BERT model implementation inspired by Hugging Face Transformers
- NewsAPI for real-time news data
- Font Awesome for icons
- WeasyPrint for PDF generation
