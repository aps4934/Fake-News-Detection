#!/usr/bin/env python3
import urllib.request
import json

def test_health_endpoint():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/health') as response:
            data = json.loads(response.read().decode())
            print("✅ Health endpoint working:", data)
            return True
    except Exception as e:
        print("❌ Health endpoint failed:", e)
        return False

def test_home_page():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/') as response:
            html = response.read().decode()
            if 'Fake News Detector' in html:
                print("✅ Home page working - contains 'Fake News Detector'")
                return True
            else:
                print("❌ Home page missing expected content")
                return False
    except Exception as e:
        print("❌ Home page failed:", e)
        return False

def test_prediction_page():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/prediction') as response:
            html = response.read().decode()
            if 'AI-Powered Fake News Detection' in html and 'Enter a news headline' in html:
                print("✅ Prediction page working - contains expected elements")
                return True
            else:
                print("❌ Prediction page missing expected content")
                return False
    except Exception as e:
        print("❌ Prediction page failed:", e)
        return False

def test_api_predict():
    try:
        data = json.dumps({"text": "This is a test news headline"}).encode('utf-8')
        req = urllib.request.Request('http://127.0.0.1:5000/api/predict',
                                   data=data,
                                   headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            if 'prediction' in result and 'confidence' in result:
                print("✅ API predict endpoint working:", result)
                return True
            else:
                print("❌ API predict endpoint returned unexpected format")
                return False
    except Exception as e:
        print("❌ API predict endpoint failed:", e)
        return False

def test_api_fetch_news():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/api/fetch_news') as response:
            data = json.loads(response.read().decode())
            if 'articles' in data:
                print("✅ API fetch news endpoint working - returned", len(data['articles']), "articles")
                return True
            else:
                print("❌ API fetch news endpoint returned unexpected format")
                return False
    except Exception as e:
        print("❌ API fetch news endpoint failed:", e)
        return False

def test_news_page():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/news') as response:
            html = response.read().decode()
            if 'Latest News' in html and 'Search for specific topics' in html:
                print("✅ News page working - contains expected elements")
                return True
            else:
                print("❌ News page missing expected content")
                return False
    except Exception as e:
        print("❌ News page failed:", e)
        return False

def test_extension_page():
    try:
        with urllib.request.urlopen('http://127.0.0.1:5000/extension') as response:
            html = response.read().decode()
            if 'Browser Extension' in html and 'Download Extension' in html:
                print("✅ Extension page working - contains expected elements")
                return True
            else:
                print("❌ Extension page missing expected content")
                return False
    except Exception as e:
        print("❌ Extension page failed:", e)
        return False

if __name__ == "__main__":
    print("🧪 Testing Fake News Detection Application...")
    print("=" * 50)

    tests = [
        test_health_endpoint,
        test_home_page,
        test_prediction_page,
        test_api_predict,
        test_api_fetch_news,
        test_news_page,
        test_extension_page
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Test Results: {passed}/{len(tests)} tests passed")

    if passed == len(tests):
        print("🎉 All tests passed! The application is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the application.")
