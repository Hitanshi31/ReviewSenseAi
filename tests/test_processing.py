import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import clean_text

examples = [
    "Great phone!",
    "<div>Amazing Phone</div>",
    "Visit https://amazon.com now",
    "   Hello     World   ",
    "Café",
]

for text in examples:
    print("Original :", repr(text))
    print("Cleaned  :", repr(clean_text(text)))
    print("-" * 40)


try:
    clean_text("")
except Exception as e:
    print(type(e).__name__, ":", e)

try:
    clean_text("      ")
except Exception as e:
    print(type(e).__name__, ":", e)

try:
    clean_text(123)
except Exception as e:
    print(type(e).__name__, ":", e)