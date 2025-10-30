import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pickle
import os

class BERTFakeNewsDetector:
    def __init__(self, model_path=None):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
        self.model.to(self.device)

        if model_path and os.path.exists(model_path):
            self.load_model(model_path)

    def preprocess_text(self, text):
        """Preprocess text for BERT input"""
        inputs = self.tokenizer(
            text,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        return inputs

    def predict(self, text):
        """Predict if news is fake or real"""
        self.model.eval()

        inputs = self.preprocess_text(text)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=1)

        # Convert prediction to label
        label = "REAL" if predictions.item() == 1 else "FAKE"
        return label

    def predict_batch(self, texts):
        """Predict for multiple texts"""
        predictions = []
        for text in texts:
            pred = self.predict(text)
            predictions.append(pred)
        return predictions

    def save_model(self, path):
        """Save the fine-tuned model"""
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def load_model(self, path):
        """Load a fine-tuned model"""
        self.model = BertForSequenceClassification.from_pretrained(path)
        self.tokenizer = BertTokenizer.from_pretrained(path)
        self.model.to(self.device)

# Fallback to traditional model if BERT fails
class FallbackModel:
    def __init__(self):
        try:
            self.vectorizer = pickle.load(open("vectorizer.pk", 'rb'))
            self.model = pickle.load(open("finalized_model.pk", 'rb'))
        except:
            self.vectorizer = None
            self.model = None

    def predict(self, text):
        if self.vectorizer and self.model:
            prediction = self.model.predict(self.vectorizer.transform([text]))[0]
            return "REAL" if prediction == 1 else "FAKE"
        return "UNKNOWN"

# Main detector class that uses BERT with fallback
class FakeNewsDetector:
    def __init__(self):
        try:
            self.bert_model = BERTFakeNewsDetector()
            self.use_bert = True
        except Exception as e:
            print(f"BERT model failed to load: {e}")
            self.bert_model = None
            self.fallback_model = FallbackModel()
            self.use_bert = False

    def predict(self, text):
        if self.use_bert and self.bert_model:
            return self.bert_model.predict(text)
        else:
            return self.fallback_model.predict(text)

    def predict_batch(self, texts):
        if self.use_bert and self.bert_model:
            return self.bert_model.predict_batch(texts)
        else:
            return [self.fallback_model.predict(text) for text in texts]
