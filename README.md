# ReviewSense AI

An end-to-end NLP application that analyzes customer product reviews using state-of-the-art Natural Language Processing and Transformer models.

ReviewSense AI summarizes reviews, predicts overall sentiment, extracts product aspects, performs aspect-based sentiment analysis, and generates a buying recommendation through a simple Streamlit interface.

---

## Features

- Review Summarization using Hugging Face Transformers (BART)
- Sentiment Analysis using RoBERTa
- Aspect Extraction using spaCy Noun Chunks
- Aspect-Based Sentiment Analysis
- Buying Recommendation Engine
- Interactive Streamlit Web Application

---

## Demo

### Input

Paste any customer product review into the application.

### Output

- Review Summary
- Overall Sentiment
- Confidence Score
- Buying Recommendation
- Aspect-wise Sentiment Analysis

---

## Project Structure

```text
ReviewSense-AI/
│
├── app/
│   └── app.py
│
├── data/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── summarizer.py
│   ├── sentiment.py
│   ├── aspect_extractor.py
│   ├── aspect_sentiment.py
│   └── recommendation.py
│
├── tests/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## Technologies Used

### Programming Language

- Python

### NLP Libraries

- spaCy
- Hugging Face Transformers

### Machine Learning Framework

- PyTorch

### Data Processing

- Pandas

### Web Framework

- Streamlit

---

## Models Used

| Task | Model |
|------|-------|
| Review Summarization | `facebook/bart-large-cnn` |
| Sentiment Analysis | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| Aspect Extraction | `spaCy en_core_web_sm` |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Hitanshi31/ReviewSenseAI.git
```

Navigate to the project directory:

```bash
cd ReviewSense-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

---

## Run the Application

Start the Streamlit application:

```bash
streamlit run app/app.py
```

---

## Workflow

```text
Customer Review
        │
        ▼
Text Preprocessing
        │
        ▼
Review Summarization
        │
        ▼
Sentiment Analysis
        │
        ▼
Aspect Extraction
        │
        ▼
Aspect-Based Sentiment Analysis
        │
        ▼
Buying Recommendation
```

---

## Example Output

### Review Summary

> The earbuds provide excellent sound quality and long battery life, with average microphone performance.

### Overall Sentiment

**Positive**

**Confidence Score:** 96.97%

### Buying Recommendation

**Recommended**

### Aspect Sentiment

| Aspect | Sentiment |
|---------|-----------|
| Sound Quality | Positive |
| Battery | Positive |
| Charging Case | Positive |
| Microphone | Neutral |

---

## Future Improvements

- Improve aspect extraction using transformer-based models.
- Fine-tune an Aspect-Based Sentiment Analysis (ABSA) model.
- Support batch review analysis.
- Add multilingual review support.
- Export analysis reports as PDF or CSV.
