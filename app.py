from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        question=request.form["question"]
        return render_template("test.html", result=question)
    return render_template("test.html")
if __name__ == "__main__":
    app.run(debug=True)
