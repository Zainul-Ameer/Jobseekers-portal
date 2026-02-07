
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/subagent-list")
def subagent_list():
    return render_template("subagent_list.html")



if __name__ == "__main__":
    app.run(debug=True)
    
