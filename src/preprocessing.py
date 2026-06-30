"""""
preprocessing.py

Utility functions for cleaning raw review text before it is passed
to Transformer-based NLP models.
"""

import re
import unicodedata

def _validate_text (text:str) -> None:
    """
Validate the input text.

Raises:
    TypeError...
"""
    if not isinstance(text,str):
        raise TypeError("Input should be a string")
    if not text.strip():
        raise ValueError("Input text cannot be empty or whitespace.")

def _normalize_unicode(text:str)->str:
    """
    Normalize Unicode characters.
    """
    return unicodedata.normalize('NFKC', text)

def _remove_html(text:str)-> str:
    """
    Remove HTML tags.
    """
    return re.sub(r"<.*?>", "", text)

def _remove_urls(text: str) -> str:
    """
    Remove URLs from text.
    """
    return re.sub(r"https?://\S+|www\.\S+", "", text)

def _normalize_whitespace(text: str) -> str:
    """
    Replace multiple whitespace characters with a single space
    and remove leading/trailing whitespace.
    """
    return re.sub(r"\s+", " ", text).strip()

def clean_text(text: str) -> str:
    """
    Clean raw review text.

    Pipeline:
        1. Validate input
        2. Normalize Unicode
        3. Remove HTML
        4. Remove URLs
        5. Normalize whitespace

    Args:
        text: Raw review text.

    Returns:
        Cleaned review text.
    """
    _validate_text(text)

    text = _normalize_unicode(text)
    text = _remove_html(text)
    text = _remove_urls(text)
    text = _normalize_whitespace(text)

    return text

    