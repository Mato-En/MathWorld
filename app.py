from flask import Flask, request, render_template
app = Flask(__name__)
import scrape
@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        question=request.form["question"]
        forums = {"mathoverflow": "https://mathoverflow.net", "stackexchange" : "https://math.stackexchange.com"}
        questions = scrape.initiate_scrape(question, forums)
        return render_template("test.html", result=questions)
    return render_template("test.html", result=dict())


if __name__ == "__main__":
    app.run(debug=True)
