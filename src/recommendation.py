"""
recommendation.py

Generate a buying recommendation based on overall review sentiment.
"""

from src.sentiment import SentimentAnalyzer


class RecommendationEngine:
    """
    Generate a buying recommendation from customer reviews.
    """

    def __init__(self) -> None:
        """
        Initialize the sentiment analyzer.
        """
        self._sentiment_analyzer = SentimentAnalyzer()

    def recommend(self, review: str) -> dict[str, str]:
        """
        Generate a buying recommendation.

        Args:
            review: Customer review.

        Returns:
            Dictionary containing the recommendation and reason.
        """

        result = self._sentiment_analyzer.analyze(review)
        sentiment = result["label"]

        if sentiment == "Positive":
            recommendation = "Recommended"
            reason = "Overall customer sentiment is positive."

        elif sentiment == "Negative":
            recommendation = "Not Recommended"
            reason = "Overall customer sentiment is negative."

        else:
            recommendation = "Consider with Caution"
            reason = "Customer reviews are mixed or neutral."

        return {
            "sentiment": sentiment,
            "recommendation": recommendation,
            "reason": reason,
        }