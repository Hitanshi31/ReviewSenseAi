# 🚀 ReviewSense AI

An end-to-end NLP application that analyzes Amazon product reviews using modern Transformer models.

ReviewSense AI summarizes customer reviews, performs sentiment analysis, extracts product aspects, and generates an intelligent buying recommendation based on customer feedback.

---

## 📌 Project Motivation

Online products often receive thousands of reviews, making it difficult for customers to understand the overall opinion before purchasing.

ReviewSense AI aims to solve this problem by automatically:

- Summarizing large collections of reviews
- Identifying customer sentiment
- Extracting important product aspects
- Generating an easy-to-understand buying recommendation

This project is being built as a learning journey into **Natural Language Processing (NLP)**, **Transformers**, and **Generative AI**.

---

## 🎯 Project Objectives

- Build a modern NLP pipeline from scratch
- Understand Transformer-based text processing
- Learn Hugging Face Transformers in depth
- Apply Aspect-Based Sentiment Analysis (ABSA)
- Develop a complete AI application using Streamlit

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NLTK
- spaCy
- Hugging Face Transformers
- PyTorch
- Streamlit

---

## 📂 Project Structure

```
ReviewSense-AI/
│
├── app/                # Streamlit application
├── data/               # Dataset instructions (dataset not included)
├── notebooks/          # EDA and experimentation notebooks
├── src/                # NLP pipeline implementation
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

This project uses the **Amazon Fine Food Reviews Dataset**.

Dataset Statistics:

- **568,454 customer reviews**
- Product ratings from **1–5 stars**
- Review summaries
- Full review text
- Helpfulness votes

> **Note:** The dataset is not included in this repository due to size and licensing considerations.

---

## ✅ Progress

### Completed

- [x] Project setup
- [x] Exploratory Data Analysis (EDA)
- [x] Review length feature engineering
- [x] Dataset quality assessment

### In Progress

- [ ] NLP Text Preprocessing
- [ ] Tokenization
- [ ] Transformer Pipeline

### Planned

- [ ] Review Summarization
- [ ] Sentiment Analysis
- [ ] Aspect Extraction
- [ ] Aspect-Based Sentiment Analysis
- [ ] Buying Recommendation Engine
- [ ] Streamlit Web Application

---

## 📈 Current Insights

Exploratory Data Analysis revealed several interesting observations:

- The dataset contains **very few missing values**.
- Customer ratings are heavily skewed toward **5-star reviews**.
- The average review contains approximately **80 words**.
- **3-star reviews** are the longest on average, suggesting customers with mixed experiences provide more detailed feedback.
- No completely duplicated records were found, although repeated review texts exist across products.

---

## 🚧 Roadmap

- Complete modern NLP preprocessing
- Implement Transformer tokenization
- Build review summarization using Hugging Face
- Develop sentiment analysis pipeline
- Implement aspect extraction
- Generate intelligent buying recommendations
- Deploy with Streamlit

---

## 🎓 Learning Goals

This project focuses on understanding the concepts behind modern NLP rather than simply using pre-built APIs.

Topics explored include:

- Tokenization
- Word Embeddings
- Attention Mechanism
- Transformers
- Hugging Face
- Aspect-Based Sentiment Analysis
- Large Language Models

---

## 📬 Future Improvements

- Fine-tuning Transformer models
- Multi-product comparison
- Review quality scoring
- Retrieval-Augmented Generation (RAG)
- LLM-powered recommendations

---

## ⭐ Status

**Currently under active development.**
