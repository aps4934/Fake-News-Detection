A modern, professional web application built with Python Flask for detecting fake news using advanced machine learning models. Features a beautiful, responsive UI with comprehensive documentation and PDF report generation.

## 🚀 Features

- **AI-Powered Detection**: Predict whether a news headline is real or fake using a pre-trained ML model with 95%+ accuracy
- **Modern UI/UX**: Beautiful, responsive design with dark theme and smooth animations
- **PDF Report Generation**: Generate professional PDF reports of your analysis results
- **Comprehensive Sections**: How It Works, Project Details, Contact information, and technical specifications
- **Health Check Endpoint**: Built-in health monitoring for deployment
- **Professional Design**: Modern interface with Tailwind CSS styling
- **Mobile Responsive**: Works perfectly on all devices
- **Fast Processing**: Real-time predictions with sub-second response times
>>>>>>> 8f8e5e1 (Initial commit)

## ⚙️ Installation (Local Setup)

### Clone the repository

```bash
git clone https://github.com/aps4934/Fake-News-Detection.git
cd Fake-News-Detection
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

<<<<<<< HEAD
=======
## 🔧 API Endpoints

### Main Routes
- `GET /` - Home page with comprehensive information about the project
- `GET/POST /prediction` - Fake news detection interface
- `POST /generate_report` - Generate PDF report of analysis results
- `GET /health` - Health check endpoint for monitoring

### PDF Report Generation
The application now includes professional PDF report generation:

```bash
curl -X POST http://localhost:5000/generate_report \
  -d "news=Your news headline here" \
  -o fake_news_report.pdf
```

## 🎨 User Interface Features

### Home Page Sections
- **Hero Section**: Welcome message with call-to-action buttons
- **Features**: Why choose our fake news detector
- **How It Works**: Step-by-step process explanation
- **Project Details**: Technology stack, model information, and key features
- **Contact**: Contact information and links to GitHub

### Prediction Page Features
- **Dual Action Buttons**: Detect fake news and generate PDF report
- **Model Explanation**: Detailed information about how the AI works
- **Performance Metrics**: Accuracy rates and processing times
- **Professional Contact Information**: Links to GitHub, documentation, and support

>>>>>>> 8f8e5e1 (Initial commit)
## 🌐 Deployment

1. Push your code to GitHub (make sure requirements.txt and Procfile are included).
2. Deploy on Heroku or similar platform using the Procfile.
<<<<<<< HEAD
=======
## 🛠 Technology Stack

### Backend
- **Python Flask**: Web framework for the application
- **Scikit-learn**: Machine learning library for the fake news detection model
- **WeasyPrint**: PDF generation for professional reports
- **Pickle**: Model serialization for fast loading
- **Gunicorn**: WSGI server for production deployment

### Frontend
- **HTML5**: Semantic markup structure
- **Tailwind CSS**: Utility-first CSS framework for modern styling
- **JavaScript**: Interactive functionality for PDF generation
- **Responsive Design**: Mobile-first approach with breakpoints

### Machine Learning
- **TF-IDF Vectorization**: Feature extraction from text data
- **Classification Algorithms**: Trained on thousands of news articles
- **Cross-validation**: Ensures model reliability and accuracy
- **Real-time Processing**: Sub-second prediction times
>>>>>>> 8f8e5e1 (Initial commit)

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py               # Flask backend application
├── requirements.txt     # Python dependencies
├── Procfile             # For deployment
├── finalized_model.pk   # Pre-trained ML model
├── vectorizer.pk        # TF-IDF vectorizer
├── news.csv             # Dataset
├── Fake news.ipynb      # Jupyter notebook for model training/experiments
│
├── templates/           # HTML templates
│   ├── index.html
│   └── prediction.html
│
└── static/              # Static files (images, etc.)
    ├── image.svg
    └── image2.svg
```

<<<<<<< HEAD
Deployed Link: https://fake-news-detection-1-vgdh.onrender.com/

## 👤 Creator

Created by Aditya Pratap Singh.
Feel free to open issues or submit pull requests for improvements!

## 📜 License

=======
## 👤 Creator

Created by Aditya Pratap Singh (aps4934).  
Email: sadityapratap070@gmail.com  
LinkedIn: https://www.linkedin.com/in/aps4934g/  
Feel free to open issues or submit pull requests for improvements!

## 📜 License

>>>>>>> 8f8e5e1 (Initial commit)
This project is licensed under the MIT License.
=======
# Fake News Detection 📰🤖

A modern, professional web application built with Python Flask for detecting fake news using advanced machine learning models. Features a beautiful, responsive UI with comprehensive documentation and PDF report generation.

## 🚀 Features

- **AI-Powered Detection**: Predict whether a news headline is real or fake using a pre-trained ML model with 95%+ accuracy
- **Modern UI/UX**: Beautiful, responsive design with dark theme and smooth animations
- **PDF Report Generation**: Generate professional PDF reports of your analysis results
- **Comprehensive Sections**: How It Works, Project Details, Contact information, and technical specifications
- **Health Check Endpoint**: Built-in health monitoring for deployment
- **Professional Design**: Modern interface with Tailwind CSS styling
- **Mobile Responsive**: Works perfectly on all devices
- **Fast Processing**: Real-time predictions with sub-second response times

## ⚙️ Installation (Local Setup)

### Clone the repository

```bash
git clone https://github.com/aps4934/Fake-News-Detection.git
cd Fake-News-Detection
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

## 🔧 API Endpoints

### Main Routes
- `GET /` - Home page with comprehensive information about the project
- `GET/POST /prediction` - Fake news detection interface
- `POST /generate_report` - Generate PDF report of analysis results
- `GET /health` - Health check endpoint for monitoring

### PDF Report Generation
The application now includes professional PDF report generation:

```bash
curl -X POST http://localhost:5000/generate_report \
  -d "news=Your news headline here" \
  -o fake_news_report.pdf
```

## 🎨 User Interface Features

### Home Page Sections
- **Hero Section**: Welcome message with call-to-action buttons
- **Features**: Why choose our fake news detector
- **How It Works**: Step-by-step process explanation
- **Project Details**: Technology stack, model information, and key features
- **Contact**: Contact information and links to GitHub

### Prediction Page Features
- **Dual Action Buttons**: Detect fake news and generate PDF report
- **Model Explanation**: Detailed information about how the AI works
- **Performance Metrics**: Accuracy rates and processing times
- **Professional Contact Information**: Links to GitHub, documentation, and support

## 🌐 Deployment

1. Push your code to GitHub (make sure requirements.txt and Procfile are included).
2. Deploy on Heroku or similar platform using the Procfile.

Deployed Link: https://fake-news-detection-1-vgdh.onrender.com/

## 🛠 Technology Stack

### Backend
- **Python Flask**: Web framework for the application
- **Scikit-learn**: Machine learning library for the fake news detection model
- **WeasyPrint**: PDF generation for professional reports
- **Pickle**: Model serialization for fast loading
- **Gunicorn**: WSGI server for production deployment

### Frontend
- **HTML5**: Semantic markup structure
- **Tailwind CSS**: Utility-first CSS framework for modern styling
- **JavaScript**: Interactive functionality for PDF generation
- **Responsive Design**: Mobile-first approach with breakpoints

### Machine Learning
- **TF-IDF Vectorization**: Feature extraction from text data
- **Classification Algorithms**: Trained on thousands of news articles
- **Cross-validation**: Ensures model reliability and accuracy
- **Real-time Processing**: Sub-second prediction times

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py               # Flask backend application
├── requirements.txt     # Python dependencies
├── Procfile             # For deployment
├── finalized_model.pk   # Pre-trained ML model
├── vectorizer.pk        # TF-IDF vectorizer
├── news.csv             # Dataset
├── Fake news.ipynb      # Jupyter notebook for model training/experiments
│
├── templates/           # HTML templates
│   ├── index.html
│   └── prediction.html
│
└── static/              # Static files (images, etc.)
    ├── image.svg
    └── image2.svg
```

## 👤 Creator

Created by Aditya Pratap Singh (aps4934).  
Email: sadityapratap070@gmail.com  
Feel free to open issues or submit pull requests for improvements!

## 📜 License

This project is licensed under the MIT License.
=======
A modern, professional web application built with Python Flask for detecting fake news using advanced machine learning models. Features a beautiful, responsive UI with comprehensive documentation and PDF report generation.

## 🚀 Features

- **AI-Powered Detection**: Predict whether a news headline is real or fake using a pre-trained ML model with 95%+ accuracy
- **Modern UI/UX**: Beautiful, responsive design with dark theme and smooth animations
- **PDF Report Generation**: Generate professional PDF reports of your analysis results
- **Comprehensive Sections**: How It Works, Project Details, Contact information, and technical specifications
- **Health Check Endpoint**: Built-in health monitoring for deployment
- **Professional Design**: Modern interface with Tailwind CSS styling
- **Mobile Responsive**: Works perfectly on all devices
- **Fast Processing**: Real-time predictions with sub-second response times
>>>>>>> 8f8e5e1 (Initial commit)

## ⚙️ Installation (Local Setup)

### Clone the repository

```bash
git clone https://github.com/aps4934/Fake-News-Detection.git
cd Fake-News-Detection
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app

```bash
python app.py
```

Open your browser at 👉 http://localhost:5000

<<<<<<< HEAD
=======
## 🔧 API Endpoints

### Main Routes
- `GET /` - Home page with comprehensive information about the project
- `GET/POST /prediction` - Fake news detection interface
- `POST /generate_report` - Generate PDF report of analysis results
- `GET /health` - Health check endpoint for monitoring

### PDF Report Generation
The application now includes professional PDF report generation:

```bash
curl -X POST http://localhost:5000/generate_report \
  -d "news=Your news headline here" \
  -o fake_news_report.pdf
```

## 🎨 User Interface Features

### Home Page Sections
- **Hero Section**: Welcome message with call-to-action buttons
- **Features**: Why choose our fake news detector
- **How It Works**: Step-by-step process explanation
- **Project Details**: Technology stack, model information, and key features
- **Contact**: Contact information and links to GitHub

### Prediction Page Features
- **Dual Action Buttons**: Detect fake news and generate PDF report
- **Model Explanation**: Detailed information about how the AI works
- **Performance Metrics**: Accuracy rates and processing times
- **Professional Contact Information**: Links to GitHub, documentation, and support

>>>>>>> 8f8e5e1 (Initial commit)
## 🌐 Deployment

1. Push your code to GitHub (make sure requirements.txt and Procfile are included).
2. Deploy on Heroku or similar platform using the Procfile.
<<<<<<< HEAD
=======

## 🛠 Technology Stack

### Backend
- **Python Flask**: Web framework for the application
- **Scikit-learn**: Machine learning library for the fake news detection model
- **WeasyPrint**: PDF generation for professional reports
- **Pickle**: Model serialization for fast loading
- **Gunicorn**: WSGI server for production deployment

### Frontend
- **HTML5**: Semantic markup structure
- **Tailwind CSS**: Utility-first CSS framework for modern styling
- **JavaScript**: Interactive functionality for PDF generation
- **Responsive Design**: Mobile-first approach with breakpoints

### Machine Learning
- **TF-IDF Vectorization**: Feature extraction from text data
- **Classification Algorithms**: Trained on thousands of news articles
- **Cross-validation**: Ensures model reliability and accuracy
- **Real-time Processing**: Sub-second prediction times
>>>>>>> 8f8e5e1 (Initial commit)

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py               # Flask backend application
├── requirements.txt     # Python dependencies
├── Procfile             # For deployment
├── finalized_model.pk   # Pre-trained ML model
├── vectorizer.pk        # TF-IDF vectorizer
├── news.csv             # Dataset
├── Fake news.ipynb      # Jupyter notebook for model training/experiments
│
├── templates/           # HTML templates
│   ├── index.html
│   └── prediction.html
│
└── static/              # Static files (images, etc.)
    ├── image.svg
    └── image2.svg
```

<<<<<<< HEAD
Deployed Link: https://fake-news-detection-1-vgdh.onrender.com/

## 👤 Creator

Created by Aditya Pratap Singh.
Feel free to open issues or submit pull requests for improvements!

## 📜 License

=======
## 👤 Creator

Created by Aditya Pratap Singh (aps4934).  
Email: sadityapratap070@gmail.com  
LinkedIn: https://www.linkedin.com/in/aps4934g/  
Feel free to open issues or submit pull requests for improvements!

## 📜 License

>>>>>>> 8f8e5e1 (Initial commit)
This project is licensed under the MIT License.
