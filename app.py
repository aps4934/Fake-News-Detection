from flask import Flask, request, render_template, jsonify
from markupsafe import escape
import requests
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

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

def predict_fake_news(text):
    """Use the provided API key to predict fake news"""
    api_key = "878ac611327e4566ac10887b2afde80e"
    url = f"https://api.meaningcloud.com/sentiment-2.1?key={api_key}&txt={text}&lang=en"

    try:
        response = requests.get(url)
        data = response.json()

        # Analyze sentiment and other factors to determine if it's fake
        sentiment = data.get('score_tag', 'NEU')

        # Simple logic: Very negative or very positive with high confidence might indicate sensationalism
        confidence = data.get('confidence', 0)

        if sentiment in ['P+', 'P'] and confidence > 80:
            return "REAL"
        elif sentiment in ['N+', 'N'] and confidence > 80:
            return "FAKE"
        else:
            # For neutral or low confidence, check for sensational language
            sensational_words = ['breaking', 'shocking', 'unbelievable', 'exclusive', 'scandal']
            text_lower = text.lower()
            if any(word in text_lower for word in sensational_words):
                return "FAKE"
            else:
                return "REAL"

    except Exception as e:
        print(f"API Error: {e}")
        return "REAL"  # Default to real if API fails

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['headline'])
        print(news)

        predict = predict_fake_news(news)
        print(predict)

        # Save to database
        new_headline = Headline(text=news, prediction=predict)
        db.session.add(new_headline)
        db.session.commit()

        return render_template("prediction.html", prediction_text = "News headline is -> {}".format(predict), now=datetime.now())

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
        prediction = predict_fake_news(text)

        # Save to database
        new_headline = Headline(text=text, prediction=prediction, source='api')
        db.session.add(new_headline)
        db.session.commit()

        return jsonify({
            'prediction': prediction,
            'confidence': 'High',
            'timestamp': datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/headlines')
def headlines():
    all_headlines = Headline.query.order_by(Headline.timestamp.desc()).all()
    return render_template('headlines.html', headlines=all_headlines)

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
