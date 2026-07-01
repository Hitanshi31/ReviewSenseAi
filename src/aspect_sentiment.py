"""
aspect_sentiment.py

Perform aspect-based sentiment analysis by combining
aspect extraction and sentiment analysis.
"""

from src.aspect_extractor import AspectExtractor
from src.sentiment import SentimentAnalyzer


class AspectSentimentAnalyzer:
    """
    Analyze the sentiment of individual product aspects.
    """

    def __init__(self) -> None:
        """
        Initialize the aspect extractor and sentiment analyzer.
        """
        self._aspect_extractor = AspectExtractor()
        self._sentiment_analyzer = SentimentAnalyzer()

    def analyze(self, review: str) -> dict[str, str]:
        """
        Analyze the sentiment of each extracted aspect.

        Args:
            review: Customer review.

        Returns:
            Dictionary mapping aspects to sentiments.
        """

        aspects = self._aspect_extractor.extract_aspects(review)

        sentences = [
            sentence.strip()
            for sentence in review.split(".")
            if sentence.strip()
        ]

        aspect_sentiments: dict[str, str] = {}

        for aspect in aspects:
            sentiment_label = "Unknown"

            for sentence in sentences:
                if aspect in sentence.lower():
                    sentiment_result = self._sentiment_analyzer.analyze(sentence)
                    sentiment_label = sentiment_result["label"]
                    break

            aspect_sentiments[aspect] = sentiment_label

        return aspect_sentiments