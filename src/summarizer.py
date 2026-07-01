"""
summarizer.py

Review summarization using Hugging Face Transformers.
"""

from transformers import pipeline
from src.preprocessing import clean_text

class ReviewSummarizer:
    """
    A class for generating summaries from customer reviews.
    """

    def __init__(self) -> None:
        """
        Initialize the summarization pipeline.
        """
        print("Loading summarization model...")
        self._summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn")
        print("Model loaded successfully.")

    def summarize(self, text: str) -> str:
        """
        Generate a summary of the input review text.

        Args:
            text: Raw customer reviews.

        Returns:
            Generated summary.
        """
        cleaned_text = clean_text(text)

        result = self._summarizer(
            cleaned_text,
            max_length=80,
            min_length=20,
            do_sample=False,
        )

        return result[0]["summary_text"]