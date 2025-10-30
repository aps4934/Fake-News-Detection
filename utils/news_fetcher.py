import requests
from newsapi import NewsApiClient
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class NewsFetcher:
    def __init__(self):
        self.api_key = os.getenv('NEWS_API_KEY')
        if self.api_key:
            self.newsapi = NewsApiClient(api_key=self.api_key)
        else:
            self.newsapi = None
            print("Warning: NEWS_API_KEY not found. News fetching will be limited.")

    def get_top_headlines(self, country='us', category=None, page_size=10):
        """Fetch top headlines from NewsAPI"""
        if not self.newsapi:
            return self._get_mock_headlines()

        try:
            if category:
                response = self.newsapi.get_top_headlines(
                    country=country,
                    category=category,
                    page_size=page_size
                )
            else:
                response = self.newsapi.get_top_headlines(
                    country=country,
                    page_size=page_size
                )

            return self._format_articles(response.get('articles', []))
        except Exception as e:
            print(f"Error fetching news: {e}")
            return self._get_mock_headlines()

    def search_news(self, query, language='en', sort_by='relevancy', page_size=10):
        """Search for news articles"""
        if not self.newsapi:
            return self._get_mock_headlines()

        try:
            # Calculate date range (last 7 days)
            from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

            response = self.newsapi.get_everything(
                q=query,
                language=language,
                sort_by=sort_by,
                from_param=from_date,
                page_size=page_size
            )

            return self._format_articles(response.get('articles', []))
        except Exception as e:
            print(f"Error searching news: {e}")
            return self._get_mock_headlines()

    def get_sources(self, category=None, language='en', country=None):
        """Get available news sources"""
        if not self.newsapi:
            return []

        try:
            response = self.newsapi.get_sources(
                category=category,
                language=language,
                country=country
            )
            return response.get('sources', [])
        except Exception as e:
            print(f"Error fetching sources: {e}")
            return []

    def _format_articles(self, articles):
        """Format articles for consistent output"""
        formatted_articles = []

        for article in articles:
            if article.get('title') and article.get('description'):
                formatted_article = {
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'content': article.get('content', ''),
                    'url': article.get('url', ''),
                    'urlToImage': article.get('urlToImage', ''),
                    'publishedAt': article.get('publishedAt', ''),
                    'source': article.get('source', {}).get('name', ''),
                    'author': article.get('author', ''),
                    'full_text': f"{article.get('title', '')}. {article.get('description', '')}"
                }
                formatted_articles.append(formatted_article)

        return formatted_articles

    def _get_mock_headlines(self):
        """Return mock headlines when API is not available"""
        return [
            {
                'title': 'Breaking: Major Scientific Discovery Announced',
                'description': 'Scientists have made a groundbreaking discovery that could change our understanding of the universe.',
                'content': 'In a press conference today, researchers announced...',
                'url': '#',
                'urlToImage': '',
                'publishedAt': datetime.now().isoformat(),
                'source': 'Science News',
                'author': 'Dr. Jane Smith',
                'full_text': 'Breaking: Major Scientific Discovery Announced. Scientists have made a groundbreaking discovery that could change our understanding of the universe.'
            },
            {
                'title': 'Technology Giant Unveils New AI Model',
                'description': 'A leading tech company has released their latest artificial intelligence model with unprecedented capabilities.',
                'content': 'The new AI model demonstrates remarkable performance...',
                'url': '#',
                'urlToImage': '',
                'publishedAt': datetime.now().isoformat(),
                'source': 'Tech Daily',
                'author': 'John Tech',
                'full_text': 'Technology Giant Unveils New AI Model. A leading tech company has released their latest artificial intelligence model with unprecedented capabilities.'
            }
        ]

# Alternative news sources (fallback)
class AlternativeNewsFetcher:
    def __init__(self):
        self.sources = [
            'https://rss.cnn.com/rss/edition.rss',
            'https://feeds.bbci.co.uk/news/rss.xml',
            'https://feeds.npr.org/1001/rss.xml'
        ]

    def fetch_from_rss(self, url):
        """Fetch news from RSS feeds"""
        try:
            import feedparser
            feed = feedparser.parse(url)
            articles = []

            for entry in feed.entries[:10]:  # Limit to 10 articles
                article = {
                    'title': entry.title,
                    'description': entry.description if hasattr(entry, 'description') else '',
                    'content': entry.summary if hasattr(entry, 'summary') else '',
                    'url': entry.link,
                    'urlToImage': '',
                    'publishedAt': entry.published if hasattr(entry, 'published') else datetime.now().isoformat(),
                    'source': feed.feed.title if hasattr(feed.feed, 'title') else 'Unknown',
                    'author': entry.author if hasattr(entry, 'author') else '',
                    'full_text': f"{entry.title}. {entry.description if hasattr(entry, 'description') else ''}"
                }
                articles.append(article)

            return articles
        except Exception as e:
            print(f"Error fetching RSS: {e}")
            return []
