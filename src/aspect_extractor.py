"""
aspect_extractor.py

Extract product aspects from customer reviews using spaCy noun chunks.
"""

import spacy

from src.preprocessing import clean_text


class AspectExtractor:
    """
    Extract candidate product aspects from customer reviews.
    """

    def __init__(self) -> None:
        """
        Load the spaCy English language model.
        """
        print("Loading spaCy model...")

        self._nlp = spacy.load("en_core_web_sm")

        print("spaCy model loaded successfully.")

    def extract_aspects(self, text: str) -> list[str]:
        """
        Extract candidate product aspects using noun chunks.

        Args:
            text: Customer review.

        Returns:
            List of extracted aspects.
        """

        cleaned_text = clean_text(text)
        doc = self._nlp(cleaned_text)

        aspects: list[str] = []

        for chunk in doc.noun_chunks:
            aspect = chunk.text.strip().lower()

            if aspect and aspect not in aspects:
                aspects.append(aspect)

        return aspects