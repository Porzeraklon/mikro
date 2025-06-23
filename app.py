import json
import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "b0d9cbf5d8afe95b7d45fa08cd61d2fc4c94c2b443c5734710f1f42a340ad355"

closed = []
question = {}
def getQuestions(file):
    closed.clear()
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for question in data:
        if question["type"] == "closed":
            closed.append(question)



@app.route('/mikro', methods=['GET', 'POST'])
def index():
    getQuestions("mikro.json")
    if request.method == 'GET':
        result = ""
        answered = False
        question = random.choice(closed)
        session["question"] = question
    
    if request.method == 'POST':
        answered = True
        answer = request.form.get('answer')
        question = session.get("question")
        correct = question["answer"]
        if answer == correct:
            result = "Poprawna odpowiedz!"
        else:
            result = f"Błąd! Poprawna odpowiedź: {correct}"
    
    return render_template('index.html', question=question, answered=answered, result=result)

if __name__ == '__main__':
    app.run(debug=False)