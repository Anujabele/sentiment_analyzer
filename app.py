from flask import Flask, render_template, request
from model import analyze_sentiment
from database import save_review, get_sentiment_distribution

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["review"]
        result = analyze_sentiment(text)
        save_review(text, result)
        chart_data = get_sentiment_distribution()
        return render_template("result.html", review=text, result=result, chart_data=chart_data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
