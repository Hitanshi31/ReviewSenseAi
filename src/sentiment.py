"""
sentiment.py

Sentiment analysis using Hugging Face Transformers.
"""

from transformers import pipeline
from src.preprocessing import clean_text

class SentimentAnalyzer:
    """
    Analyze customer review sentiment.
    """

    def __init__(self) -> None:
        """
        Initialize the sentiment analysis pipeline.
        """

        print("Loading sentiment model..")

        self.classifier = pipeline(
            task = "sentiment-analysis",
            model = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        )

        print ("Sentiment model loaded successfully.")

    def analyze(self, text: str) -> dict:
        """
        Analyze the sentiment of the input text.

        Args:
         text: Customer review.

        Returns:
        
        Dictionary containing sentiment label and confidence score.
        """
    
        cleaned_text = clean_text(text)
        result = self.classifier(cleaned_text)

        return result[0]