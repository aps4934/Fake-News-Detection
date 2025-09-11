# Fake News Detection 📰🤖

A web application built with Python Flask for detecting fake news using machine learning models.

## 🚀 Features

- Predict whether a news headline is real or fake using a pre-trained ML model.
- Simple web interface for inputting news text.
- Built with Flask backend and HTML templates.
- Ready for deployment on platforms like Heroku.

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

## 🌐 Deployment

1. Push your code to GitHub (make sure requirements.txt and Procfile are included).
2. Deploy on Heroku or similar platform using the Procfile.

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

Deployed Link: https://fake-news-detection-1-vgdh.onrender.com/

## 👤 Creator

Created by Aditya Pratap Singh.
Feel free to open issues or submit pull requests for improvements!

## 📜 License

This project is licensed under the MIT License.
