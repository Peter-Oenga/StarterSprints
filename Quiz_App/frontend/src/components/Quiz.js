import React, { useState } from "react";

function Quiz({ questions, endQuiz }) {
  const [userAnswers, setUserAnswers] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

  const handleAnswerChange = (question, answer) => {
    setUserAnswers({
      ...userAnswers,
      [question]: answer,
    });
  };

  const handleNext = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      endQuiz(userAnswers);
    }
  };

  const question = questions[currentQuestionIndex];

  return (
    <div className="quiz">
      <h2>{question.question}</h2>
      <div className="options">
        {question.options.map((option) => (
          <button
            key={option}
            onClick={() => handleAnswerChange(question.question, option)}
          >
            {option}
          </button>
        ))}
      </div>
      <button onClick={handleNext}>Next</button>
    </div>
  );
}

export default Quiz;
