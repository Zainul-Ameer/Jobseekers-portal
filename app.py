# app.py - A simple Flask application that serves an HTML template.
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    
    
# this code sets up a basic Flask application that listens for requests on the root URL ("/") and responds by rendering an HTML template called "index.html". The application is run in debug mode, which allows for easier development and troubleshooting

# To run this application, you would need to have Flask installed in your Python environment. You can install it using pip:
# pip install Flask 
