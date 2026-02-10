from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        contact = request.form["contact"]
        return f"OTP will be sent to {contact}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)