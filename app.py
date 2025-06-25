import json
import random
from flask import Flask, render_template, request, session, redirect, url_for

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

@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('menu.html')
    else:
        quiz = request.form.get('quiz')
        return redirect(url_for(quiz))

@app.route('/mikro', methods=['GET', 'POST'])
def mikro():
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

@app.route('/prawo/test', methods=['GET', 'POST'])
def prawo_test():
    getQuestions("prawo-test.json")
    if request.method == 'GET':
        result = ""
        explanation = ""
        answered = False
        question = random.choice(closed)
        session["question"] = question
    
    if request.method == 'POST':
        answered = True
        answer = request.form.get('answer')
        question = session.get("question")
        correct = question["answer"]
        explanation = question["explanation"]
        if answer == correct:
            result = "Poprawna odpowiedz!"
        else:
            result = f"Błąd! Poprawna odpowiedź: {correct}"
    
    return render_template('test.html', question=question, answered=answered, result=result, explanation=explanation)

@app.route('/prawo/baza', methods=['GET', 'POST'])
def prawo_baza():
    getQuestions("prawo-baza.json")
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