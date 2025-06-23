import json
import random
from flask import Flask, render_template, request
#test
app = Flask(__name__)

@app.route('/mikro', methods=['GET', 'POST'])
def index():

    closed = []
    question = {}
    def getQuestions():

        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for question in data:
            if question["type"] == "closed":
                closed.append(question)

    getQuestions()

    if request.method == 'GET':
        result = ""
        answered = False
        question["number"] = random.randint(0, len(closed) - 1)
        question["content"] = closed[question["number"]]["question"]
        question["a"] = closed[question["number"]]["options"]["a"]
        question["b"] = closed[question["number"]]["options"]["b"]
        question["c"] = closed[question["number"]]["options"]["c"]
        question["d"] = closed[question["number"]]["options"]["d"]
        question["answer"] = closed[question["number"]]["answer"]
    
    if request.method == 'POST':
        answered = True
        answer = request.form.get('answer')
        correct = question["answer"]
        if answer == correct:
            result = "Poprawna odpowiedz!"
        else:
            result = "Błąd! Poprawna odpowiedź: " + correct
    
    return render_template('index.html', question=question, answered=answered, result=result)

if __name__ == '__main__':
    app.run(debug=True)