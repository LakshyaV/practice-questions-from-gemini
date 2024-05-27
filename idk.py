from flask import Flask, render_template, request
from pypdf import PdfReader
from question_gen import generate_questions
from langchain_google_genai import ChatGoogleGenerativeAI
import re

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    questions = ""
    text = ""
    if request.method == "POST":
        pdf = request.files["pdf"]
        data = PdfReader(pdf)
        for page in data.pages:
            text += page.extract_text()
        subject = request.form['subject']
        number = request.form['number']
        difficulty = request.form['Difficulty']
        questions = generate_questions(subject, number, difficulty, text)
    
    return render_template("index.html", questions=questions)

@app.route("/questioner")
def questioner():
    return "Page Two!"

if __name__ == "__main__":
    app.run(debug=True)
