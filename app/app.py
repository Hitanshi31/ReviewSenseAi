"""
Streamlit application for ReviewSense AI.
"""

import pandas as pd
import streamlit as st

from src.summarizer import ReviewSummarizer
from src.sentiment import SentimentAnalyzer
from src.aspect_sentiment import AspectSentimentAnalyzer
from src.recommendation import RecommendationEngine


st.set_page_config(
    page_title="ReviewSense AI",
    layout="wide",
)


@st.cache_resource
def load_models():
    """
    Load NLP models once and cache them.
    """
    return {
        "summarizer": ReviewSummarizer(),
        "sentiment": SentimentAnalyzer(),
        "aspect_sentiment": AspectSentimentAnalyzer(),
        "recommender": RecommendationEngine(),
    }


models = load_models()

st.title("ReviewSense AI")
st.caption("Intelligent Product Review Analysis using NLP and Transformers")


review = st.text_area(
    "Customer Review",
    height=220,
    placeholder="Paste a product review here...",
)


if st.button("Analyze Review", use_container_width=True):

    if not review.strip():
        st.warning("Please enter a review.")
        st.stop()

    with st.spinner("Analyzing review..."):

        try:

            summary = models["summarizer"].summarize(review)

            sentiment_result = models["sentiment"].analyze(review)

            aspect_results = models["aspect_sentiment"].analyze(review)

            recommendation = models["recommender"].recommend(review)

        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.divider()

    st.subheader("Review Summary")
    st.write(summary)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Overall Sentiment")

        st.metric(
            label="Sentiment",
            value=sentiment_result["label"],
        )

        st.caption(
            f"Confidence Score: {sentiment_result['score']:.2%}"
        )

    with col2:
        st.subheader("Buying Recommendation")

        st.metric(
            label="Recommendation",
            value=recommendation["recommendation"],
        )

        st.caption(recommendation["reason"])

    st.divider()

    st.subheader("Aspect Sentiment")

    if aspect_results:

        df = pd.DataFrame(
            {
                "Aspect": list(aspect_results.keys()),
                "Sentiment": list(aspect_results.values()),
            }
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.info("No aspect sentiments found.")