import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.summarizer import ReviewSummarizer

summarizer = ReviewSummarizer()

reviews = """
The battery life is excellent and lasts more than a full day with heavy use.
The display is bright, vibrant, and easy to read even outdoors.
The camera captures sharp and detailed photos during the day.
Night photography is decent but could be improved.
The phone feels premium and is comfortable to hold.
Charging is very fast, reaching 100 in under an hour.
The speakers are loud and clear.
The software experience is smooth with almost no lag.
Some users felt that the phone is slightly overpriced.
However, most customers were satisfied with the overall performance.
Many reviewers recommended this phone because of its battery life and camera quality.
Overall, the phone provides excellent value despite its higher price.
"""

summary = summarizer.summarize(reviews)

print(summary)