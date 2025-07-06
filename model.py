from transformers import pipeline

# Load sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    label = result['label'].lower()
    if label == "negative":
        sentiment = "negative"
    elif label == "positive":
        sentiment = "positive"
    else:
        sentiment = "neutral"
    return {
        "label": sentiment,
        "score": round(result["score"], 2)
    }
