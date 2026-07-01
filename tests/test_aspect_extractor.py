from src.aspect_extractor import AspectExtractor

extractor = AspectExtractor()

review = (
    "The battery life is amazing, "
    "the camera quality is excellent, "
    "and the display is bright."
)

print(extractor.extract_aspects(review))