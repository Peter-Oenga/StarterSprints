import os
from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)

# Ensure the quiz_data.json file is in the correct path
base_dir = os.path.dirname(os.path.abspath(__file__))
quiz_data_path = os.path.join(base_dir, 'quiz_data.json')

# Load quiz questions from the JSON file
with open(quiz_data_path) as f:
    quiz_data = json.load(f)

@app.route('/api/questions', methods=['GET'])
def get_questions():
    random.shuffle(quiz_data)  # Shuffle the questions for randomness
    return jsonify(quiz_data)

@app.route('/api/submit_answers', methods=['POST'])
def submit_answers():
    user_answers = request.json
    score = 0
    for question, answer in user_answers.items():
        correct_answer = next(q['correct_answer'] for q in quiz_data if q['question'] == question)
        if answer == correct_answer:
            score += 1
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(debug=True)
