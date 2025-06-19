#!/usr/bin/env python3
"""
Advanced Analysis Example
Complex scraping with data analysis, filtering, and reporting.
"""

import os
import json
import csv
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from dotenv import load_dotenv
import serp_forge as sf

# Load environment variables
load_dotenv()

class ContentAnalyzer:
    """Advanced content analysis and reporting."""
    
    def __init__(self):
        self.articles = []
        self.sentiment_stats = defaultdict(int)
        self.source_stats = Counter()
        self.keyword_stats = Counter()
        self.date_stats = defaultdict(int)
    
    def add_articles(self, articles):
        """Add articles for analysis."""
        self.articles.extend(articles)
    
    def analyze_sentiment_distribution(self):
        """Analyze sentiment distribution."""
        for article in self.articles:
            if article.sentiment:
                self.sentiment_stats[article.sentiment] += 1
    
    def analyze_sources(self):
        """Analyze source distribution."""
        for article in self.articles:
            self.source_stats[article.source] += 1
    
    def analyze_keywords(self):
        """Analyze keyword frequency."""
        for article in self.articles:
            if article.keywords:
                for keyword in article.keywords:
                    self.keyword_stats[keyword.lower()] += 1
    
    def analyze_publish_dates(self):
        """Analyze publish date distribution."""
        for article in self.articles:
            if article.publish_date:
                # Group by week
                week_start = article.publish_date - timedelta(days=article.publish_date.weekday())
                week_key = week_start.strftime("%Y-%m-%d")
                self.date_stats[week_key] += 1
    
    def generate_report(self):
        """Generate comprehensive analysis report."""
        self.analyze_sentiment_distribution()
        self.analyze_sources()
        self.analyze_keywords()
        self.analyze_publish_dates()
        
        report = {
            "summary": {
                "total_articles": len(self.articles),
                "articles_with_sentiment": sum(1 for a in self.articles if a.sentiment),
                "articles_with_keywords": sum(1 for a in self.articles if a.keywords),
                "unique_sources": len(self.source_stats),
                "date_range": self._get_date_range()
            },
            "sentiment_analysis": dict(self.sentiment_stats),
            "top_sources": dict(self.source_stats.most_common(10)),
            "top_keywords": dict(self.keyword_stats.most_common(20)),
            "publish_timeline": dict(self.date_stats),
            "quality_metrics": self._calculate_quality_metrics()
        }
        
        return report
    
    def _get_date_range(self):
        """Get the date range of articles."""
        dates = [a.publish_date for a in self.articles if a.publish_date]
        if dates:
            return {
                "earliest": min(dates).isoformat(),
                "latest": max(dates).isoformat()
            }
        return None
    
    def _calculate_quality_metrics(self):
        """Calculate quality metrics."""
        word_counts = [a.word_count for a in self.articles if a.word_count > 0]
        quality_scores = [a.quality_score for a in self.articles if a.quality_score]
        
        return {
            "avg_word_count": sum(word_counts) / len(word_counts) if word_counts else 0,
            "avg_quality_score": sum(quality_scores) / len(quality_scores) if quality_scores else 0,
            "articles_with_author": sum(1 for a in self.articles if a.author),
            "articles_with_summary": sum(1 for a in self.articles if a.summary)
        }

def search_and_analyze(query: str, max_results: int = 10):
    """Search and analyze content for a specific query."""
    print(f"🔍 Searching for: {query}")
    
    results = sf.scrape(
        query=query,
        search_type="web",
        max_results=max_results,
        include_content=True,
        extract_metadata=True
    )
    
    if results.success:
        print(f"   ✅ Found {len(results.results)} articles")
        return results.results
    else:
        print(f"   ❌ Search failed: {results.error_message}")
        return []

def save_to_csv(articles, filename):
    """Save articles to CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'title', 'url', 'source', 'author', 'publish_date', 
            'sentiment', 'sentiment_score', 'word_count', 'quality_score',
            'keywords', 'summary'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for article in articles:
            writer.writerow({
                'title': article.title,
                'url': str(article.url),
                'source': article.source,
                'author': article.author or '',
                'publish_date': article.publish_date.isoformat() if article.publish_date else '',
                'sentiment': article.sentiment or '',
                'sentiment_score': article.sentiment_score or 0,
                'word_count': article.word_count,
                'quality_score': article.quality_score or 0,
                'keywords': ', '.join(article.keywords) if article.keywords else '',
                'summary': article.summary or ''
            })

def main():
    """Advanced analysis example."""
    print("🔬 Advanced Analysis Example")
    print("=" * 50)
    
    # Check if API key is set
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key or api_key == "your_serper_api_key_here":
        print("❌ Error: Please set your SERPER_API_KEY in the .env file")
        return
    
    # Define research topics
    research_topics = [
        "artificial intelligence ethics",
        "machine learning applications",
        "data privacy regulations",
        "cybersecurity threats",
        "sustainable technology"
    ]
    
    print(f"📚 Researching {len(research_topics)} topics...")
    print()
    
    # Initialize analyzer
    analyzer = ContentAnalyzer()
    all_articles = []
    
    # Search and collect articles
    for topic in research_topics:
        articles = search_and_analyze(topic, max_results=5)
        analyzer.add_articles(articles)
        all_articles.extend(articles)
    
    if not all_articles:
        print("❌ No articles found for analysis")
        return
    
    print(f"\n📊 Analyzing {len(all_articles)} articles...")
    
    # Generate comprehensive report
    report = analyzer.generate_report()
    
    # Display report
    print("\n📋 Analysis Report")
    print("=" * 50)
    
    print(f"📈 Summary:")
    print(f"   Total articles: {report['summary']['total_articles']}")
    print(f"   Articles with sentiment: {report['summary']['articles_with_sentiment']}")
    print(f"   Articles with keywords: {report['summary']['articles_with_keywords']}")
    print(f"   Unique sources: {report['summary']['unique_sources']}")
    
    print(f"\n😊 Sentiment Distribution:")
    for sentiment, count in report['sentiment_analysis'].items():
        percentage = (count / report['summary']['total_articles']) * 100
        print(f"   {sentiment}: {count} ({percentage:.1f}%)")
    
    print(f"\n🌐 Top Sources:")
    for source, count in report['top_sources'].items():
        print(f"   {source}: {count} articles")
    
    print(f"\n🏷️  Top Keywords:")
    for keyword, count in report['top_keywords'].items():
        print(f"   {keyword}: {count} occurrences")
    
    print(f"\n📊 Quality Metrics:")
    metrics = report['quality_metrics']
    print(f"   Average word count: {metrics['avg_word_count']:.0f}")
    print(f"   Average quality score: {metrics['avg_quality_score']:.2f}")
    print(f"   Articles with author: {metrics['articles_with_author']}")
    print(f"   Articles with summary: {metrics['articles_with_summary']}")
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save detailed report
    report_file = f"analysis_report_{timestamp}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    # Save articles to CSV
    csv_file = f"articles_{timestamp}.csv"
    save_to_csv(all_articles, csv_file)
    
    print(f"\n💾 Results saved:")
    print(f"   📄 Analysis report: {report_file}")
    print(f"   📊 Articles data: {csv_file}")
    
    # Show insights
    print(f"\n💡 Key Insights:")
    
    # Most positive/negative topics
    positive_articles = [a for a in all_articles if a.sentiment == 'positive']
    negative_articles = [a for a in all_articles if a.sentiment == 'negative']
    
    if positive_articles:
        print(f"   😊 Most positive topic: {positive_articles[0].title[:50]}...")
    if negative_articles:
        print(f"   😞 Most negative topic: {negative_articles[0].title[:50]}...")
    
    # Longest article
    longest_article = max(all_articles, key=lambda x: x.word_count)
    print(f"   📝 Longest article: {longest_article.title[:50]}... ({longest_article.word_count} words)")
    
    # Highest quality article
    high_quality_articles = [a for a in all_articles if a.quality_score and a.quality_score > 0.8]
    if high_quality_articles:
        best_article = max(high_quality_articles, key=lambda x: x.quality_score)
        print(f"   ⭐ Highest quality: {best_article.title[:50]}... (score: {best_article.quality_score:.2f})")

if __name__ == "__main__":
    main() 