import React, { useEffect, useState } from "react";
import axios from "axios";
import Quiz from "./components/Quiz";

function App() {
  const [questions, setQuestions] = useState([]);
  const [quizStarted, setQuizStarted] = useState(false);
  const [quizEnded, setQuizEnded] = useState(false);
  const [score, setScore] = useState(0);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/questions").then((response) => {
      setQuestions(response.data);
    });
  }, []);

  const startQuiz = () => {
    setQuizStarted(true);
  };

  const endQuiz = (userAnswers) => {
    axios
      .post("http://127.0.0.1:5000/api/submit_answers", userAnswers)
      .then((response) => {
        setScore(response.data.score);
        setQuizEnded(true);
      });
  };

  return (
    <div className="app">
      {!quizStarted && !quizEnded && (
        <button onClick={startQuiz}>Start Quiz</button>
      )}

      {quizStarted && !quizEnded && (
        <Quiz questions={questions} endQuiz={endQuiz} />
      )}

      {quizEnded && <h2>Your score is: {score}</h2>}
    </div>
  );
}

export default App;
