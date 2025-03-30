import React from 'react';
import { useState } from "react";
import Spinner from "./Spinner";

function App() {
  const [joke, setJoke] = useState("Click the button to get a joke!");
  const [loading, setLoading] = useState(false);
  const [error, setError] =useState("");

  const fetchJoke = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await fetch("https://v2.jokeapi.dev/joke/Programming?type=single");

      if (!res.ok) {
        throw new Error("Failed to fetch joke");
      }

      const data = await res.json();
      setJoke(data.joke);

    } catch (err) {
      setError("Oops! Something went wrong. Try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
    
  };
  return (
    <div className='min-h-screen bg-gray-100 flex flex-col items-center justify-center px-4'>
      <h1 className='text-3xl font-bold mb-6'>
        Random Joke Generator
      </h1>

      <div className="bg-white shadow-lg rounded-lg p-6 max-w-xl w-full text-center mb-4 min-h-[100px] flex items-center justify-center">

        {loading ? (
           <Spinner />
        ) :error ? (
          <p className='text-red-500'>{error}</p>
        ) : (
          <p className='text-lg'>{joke}</p>
        
        )}

     
      </div>

      <button 
      onClick={fetchJoke}
      disabled={loading}
      className={`mt-4 px-6 py-2 rounded transition ${
        loading
          ? "bg-gray-400 cursor-not-allowed"
          : "bg-blue-500 hover:bg-blue-600 text-white"
      }` }
      >
        {loading ? "Please wait..." : "Get a Joke"}

      </button>

    </div>
  );
}

export default App;