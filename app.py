from flask import Flask, request, render_template, send_file, jsonify
from markupsafe import escape
import pickle
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.bert_model import FakeNewsDetector
from utils.news_fetcher import NewsFetcher
import json

# Initialize detector
detector = FakeNewsDetector()

# Initialize news fetcher
news_fetcher = NewsFetcher()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_headlines.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Headline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    prediction = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(100), default='manual')
    url = db.Column(db.String(500), default='')

    def __repr__(self):
        return f'<Headline {self.id}: {self.text[:50]}...>'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)

        predict = detector.predict(news)
        print(predict)

        # Save to database
        new_headline = Headline(text=news, prediction=predict)
        db.session.add(new_headline)
        db.session.commit()

        return render_template("prediction.html", prediction_text = "News headline is -> {}".format(predict))

    else:
        return render_template("prediction.html")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for browser extension and external requests"""
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text field'}), 400

        text = data['text']
        prediction = detector.predict(text)

        # Save to database
        new_headline = Headline(text=text, prediction=prediction, source='api')
        db.session.add(new_headline)
        db.session.commit()

        return jsonify({
            'prediction': prediction,
            'confidence': 'High',  # Could be enhanced with actual confidence scores
            'timestamp': datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/fetch_news', methods=['GET'])
def api_fetch_news():
    """API endpoint to fetch news from online sources"""
    try:
        category = request.args.get('category', None)
        query = request.args.get('query', None)
        limit = int(request.args.get('limit', 10))

        if query:
            articles = news_fetcher.search_news(query, page_size=limit)
        else:
            articles = news_fetcher.get_top_headlines(category=category, page_size=limit)

        return jsonify({'articles': articles})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze_news', methods=['POST'])
def api_analyze_news():
    """API endpoint to analyze multiple news articles"""
    try:
        data = request.get_json()
        if not data or 'articles' not in data:
            return jsonify({'error': 'Missing articles field'}), 400

        articles = data['articles']
        results = []

        for article in articles:
            text = article.get('full_text', article.get('title', ''))
            if text:
                prediction = detector.predict(text)
                result = {
                    'title': article.get('title', ''),
                    'prediction': prediction,
                    'url': article.get('url', ''),
                    'source': article.get('source', '')
                }
                results.append(result)

                # Save to database
                new_headline = Headline(
                    text=text[:500],  # Limit text length
                    prediction=prediction,
                    source=article.get('source', 'api'),
                    url=article.get('url', '')
                )
                db.session.add(new_headline)

        db.session.commit()

        return jsonify({'results': results})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        news = str(request.form['news'])
        prediction = detector.predict(news)

        # Create HTML content for PDF
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Fake News Detection Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .header {{ text-align: center; color: #333; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }}
                .result {{ font-size: 24px; font-weight: bold; text-align: center; margin: 30px 0; }}
                .real {{ color: #28a745; }}
                .fake {{ color: #dc3545; }}
                .details {{ margin: 20px 0; }}
                .footer {{ text-align: center; margin-top: 50px; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Fake News Detection Report</h1>
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>

            <div class="details">
                <h2>Analysis Details</h2>
                <p><strong>Input Headline:</strong> {escape(news)}</p>
                <p><strong>Prediction:</strong> <span class="result {'real' if prediction == 'REAL' else 'fake'}">{prediction}</span></p>
                <p><strong>Model:</strong> BERT-based Transformer Model</p>
                <p><strong>Confidence:</strong> High (AI-Powered Analysis)</p>
            </div>

            <div class="footer">
                <p>Report generated by Fake News Detector</p>
                <p>Created by aps4934 | https://github.com/aps4934/Fake-News-Detection</p>
            </div>
        </body>
        </html>
        """

        # Generate PDF filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        pdf_filename = f"fake_news_report_{timestamp}.pdf"

        # Generate PDF using WeasyPrint
        from weasyprint import HTML, CSS
        HTML(string=html_content).write_pdf(pdf_filename)

        # Return PDF file
        return send_file(pdf_filename, as_attachment=True, download_name=pdf_filename)

    except Exception as e:
        print(f"Error generating PDF: {e}")
        return "Error generating report", 500

@app.route('/headlines')
def headlines():
    all_headlines = Headline.query.order_by(Headline.timestamp.desc()).all()
    return render_template('headlines.html', headlines=all_headlines)

@app.route('/news')
def news():
    """Page to display fetched news"""
    return render_template('news.html')

@app.route('/extension')
def extension():
    """Page with browser extension information"""
    return render_template('extension.html')

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
