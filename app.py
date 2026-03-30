from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.mail.me.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/download/cv')
def download_cv():
    return send_from_directory('static', 'cv.pdf', as_attachment=True)

@app.route('/download/portfolio')
def download_portfolio():
    return send_from_directory('static', 'portfolio.pdf', as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = Message(
        subject=f"Portfolio Contact: {subject}",
        sender=os.getenv('MAIL_USERNAME'),
        recipients=[os.getenv('MAIL_USERNAME')]
    )
    msg.body = f"From: {name} <{email}>\n\n{message}"

    try:
        mail.send(msg)
        flash('Message sent successfully!', 'success')
    except:
        flash('Something went wrong. Please try again.', 'error')

    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)