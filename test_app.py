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
            if 'Fake News Detection' in html and 'Enter News Headline' in html:
                print("✅ Prediction page working - contains expected elements")
                return True
            else:
                print("❌ Prediction page missing expected content")
                return False
    except Exception as e:
        print("❌ Prediction page failed:", e)
        return False

if __name__ == "__main__":
    print("🧪 Testing Fake News Detection Application...")
    print("=" * 50)

    tests = [
        test_health_endpoint,
        test_home_page,
        test_prediction_page
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
