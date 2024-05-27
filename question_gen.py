import google.generativeai as genai
import pathlib
import textwrap

genai.configure(api_key="AIzaSyDE-qatlezCN53sYNnxzuR7yRpA9J7XgsM")

generation_config = genai.GenerationConfig = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)
convo = model.start_chat(history=[])

subject = ""
number = ""
difficulty = ""

def generate_questions(subject, number, difficulty, content):
    prompt = f"I am a student studying {subject} and I am looking for questions to practicefor my upcoming test. Can you please list {number} questions of {difficulty} level for me? Please only list the questions and say nothing else. Please use the content from the following lesson/information to create the questions: {content}"

    convo.send_message(prompt)
    return convo.last.text