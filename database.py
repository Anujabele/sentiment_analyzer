from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sentimentDB"]
collection = db["reviews"]

def save_review(text, result):
    doc = {
        "review": text,
        "sentiment": result["label"],
        "score": result["score"]
    }
    collection.insert_one(doc)

def get_sentiment_distribution():
    data = collection.aggregate([
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ])
    return {doc["_id"]: doc["count"] for doc in data}
