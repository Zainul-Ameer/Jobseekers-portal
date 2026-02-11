from flask import Flask, request, render_template, redirect, session
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Gmail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'za378r@gmail.com'
app.config['MAIL_PASSWORD'] = 'kkksnylyhnvlirjm'
app.config['MAIL_DEFAULT_SENDER'] = 'za378r@gmail.com'

mail = Mail(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/send_otp', methods=['POST'])
def send_otp():
    user_email = request.form.get('email')

    otp = str(random.randint(100000, 999999))

    session['otp'] = otp
    session['email'] = user_email

    msg = Message(
        subject='Your OTP Code',
        recipients=[user_email],
        body=f'Your OTP is: {otp}'
    )

    mail.send(msg)

    return redirect("/verify")


@app.route('/verify')
def verify_page():
    return render_template("verify.html")


@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    user_otp = request.form.get('otp')

    if user_otp == session.get('otp'):
        return redirect("/upload")
    else:
        return "Invalid OTP ❌"


@app.route('/upload')
def upload_page():
    return render_template("upload.html")


@app.route('/upload_cv', methods=['POST'])
def upload_cv():
    file = request.files['cv']
    user_email = session.get('email')

    if file:
        # Create folder with email name
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], user_email)

        os.makedirs(user_folder, exist_ok=True)

        file_path = os.path.join(user_folder, file.filename)
        file.save(file_path)

        return "CV uploaded successfully ✅"

    return "No file selected"


if __name__ == '__main__':
    app.run(debug=True)