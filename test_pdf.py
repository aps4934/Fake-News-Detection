#!/usr/bin/env python3
import urllib.request
import urllib.parse
import os

def test_pdf_generation():
    try:
        # Test data
        test_news = "This is a test news headline for fake news detection"

        # Prepare POST data
        data = urllib.parse.urlencode({'news': test_news}).encode()
        req = urllib.request.Request('http://127.0.0.1:5000/generate_report', data=data, method='POST')

        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                # Save the PDF
                pdf_content = response.read()
                pdf_filename = "test_fake_news_report.pdf"

                with open(pdf_filename, 'wb') as f:
                    f.write(pdf_content)

                if os.path.exists(pdf_filename) and os.path.getsize(pdf_filename) > 0:
                    print(f"✅ PDF generation working - created {pdf_filename} ({os.path.getsize(pdf_filename)} bytes)")
                    # Clean up
                    os.remove(pdf_filename)
                    return True
                else:
                    print("❌ PDF file not created properly")
                    return False
            else:
                print(f"❌ PDF generation failed with status code: {response.getcode()}")
                return False
    except Exception as e:
        print(f"❌ PDF generation failed: {e}")
        return False

def test_prediction_functionality():
    try:
        # Test data
        test_news = "Breaking news: Scientists discover new planet"

        # Prepare POST data
        data = urllib.parse.urlencode({'news': test_news}).encode()
        req = urllib.request.Request('http://127.0.0.1:5000/prediction', data=data, method='POST')

        with urllib.request.urlopen(req) as response:
            html = response.read().decode()
            if 'News headline is ->' in html or 'FAKE' in html or 'REAL' in html:
                print("✅ Prediction functionality working - response contains prediction result")
                return True
            else:
                print("❌ Prediction response missing expected content")
                print("Response preview:", html[:200] + "..." if len(html) > 200 else html)
                return False
    except Exception as e:
        print(f"❌ Prediction functionality failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Advanced Features...")
    print("=" * 50)

    tests = [
        test_pdf_generation,
        test_prediction_functionality
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Advanced Test Results: {passed}/{len(tests)} tests passed")

    if passed == len(tests):
        print("🎉 All advanced tests passed! PDF generation and prediction are working correctly.")
    else:
        print("⚠️  Some advanced tests failed. Please check the application.")
