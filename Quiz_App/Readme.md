# Quiz App

## Overview
This is a simple command-line Quiz App developed in Python. The application presents multiple-choice questions to users, allows them to input answers, and provides instant feedback. At the end of the quiz, the total score is displayed, and users can choose to play again.

## Features
- Multiple-choice questions with four options each.
- User input validation to ensure only valid choices are accepted.
- Instant feedback on correct and incorrect answers.
- Final score display at the end of the quiz.
- Option to replay the quiz.

## Requirements
Ensure you have the following installed before running the program:
- Python 3.x

## Installation
1. Clone this repository or download the script.
```sh
    git clone https://github.com/your-username/quiz-app.git
```
2. Navigate to the project directory.
```sh
    cd quiz-app
```
3. Run the script.
```sh
    python quiz.py
```

## How to Play
1. The quiz presents a question with four possible answers.
2. Enter a number between 1 and 4 to select your answer.
3. If the answer is correct, you earn a point.
4. If the answer is incorrect, the correct answer is displayed.
5. At the end of the quiz, your total score is displayed.
6. You will be prompted to play again or exit the game.

## Code Structure
- `quiz_data` contains a list of tuples with questions, choices, and the correct answer index.
- `run_quiz()` function iterates through the questions, gets user input, and evaluates responses.
- `play_again()` function prompts the user to restart the quiz or exit.

## Example Output
```
Q1: What is the capital City of Kenya?
1: Nairobi
2: Mombasa
3: Kisumu
4: Kisii
Enter an answer between 1 and 4: 1
Correct!

Your total score is 1/5
Do you want to play again? (yes/No):
```

## Potential Improvements
- Store user scores for performance tracking.
- Implement a graphical user interface (GUI).
- Add more questions and difficulty levels.
- Integrate a timer for each question.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.

