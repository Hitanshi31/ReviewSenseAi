import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()

reviews = [
    "This phone is amazing. Battery life is excellent.",
    "The product is okay. Nothing special.",
    "Worst phone I have ever bought.",
]

for review in reviews:
    result = analyzer.analyze(review)

    print("-" * 50)
    print(review)
    print(result)