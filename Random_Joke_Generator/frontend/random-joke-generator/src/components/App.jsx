import React from 'react';
import { useState, useEffect } from "react";
import Spinner from "./Spinner";

function App() {
  const [joke, setJoke] = useState("Click the button to get a joke!");
  const [loading, setLoading] = useState(false);
  const [error, setError] =useState("");
  const [category, setCategory] = useState("Programming")
  const [favorites, setFavorites] = useState([]);
  const [toastMessage, setToastMessage] = useState("");

  // Load favorites from local Storage on initial render
  useEffect(() => {
    const stored = localStorage.getItem("favoriteJokes");
    if (stored) {
      setFavorites(JSON.parse(stored));
    }
  }, []);

  // Save favorites to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem("favoriteJokes", JSON.stringify(favorites));
  }, [favorites]);


  const fetchJoke = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await fetch(`https://v2.jokeapi.dev/joke/${category}?type=single`);

      if (!res.ok) {
        throw new Error("Failed to fetch joke");
      }

      const data = await res.json();
      setJoke(data.joke || "No joke found.");

    } catch (err) {
      setError("Oops! Something went wrong. Try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
    
  };

  const saveToFavorites = () => {
    if (!favorites.includes(joke)){
      setFavorites([...favorites, joke])
    }
  };

  const handleRemove = (jokeToRemove) => {
    const updatedFavorites = favorites.filter((fav) => fav !== jokeToRemove)
    setFavorites(updatedFavorites);
    showToast("Joke Removed")
  };

  const showToast = (message) => {
    setToastMessage(message);
    setTimeout(() => setToastMessage(""), 2000);

  };

  return (

    
    <div className='min-h-screen bg-gray-100 flex flex-col items-center justify-center px-4'>
      <h1 className='text-3xl font-bold mb-6'>
        Random Joke Generator
      </h1>

      {toastMessage && (
      <div className="fixed top-4 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-4 py-2 rounded shadow z-50">
        {toastMessage}
      </div>
    )}

      
      <div className="mb-4">
        <label htmlFor='category' className='block mb-1 font-medium'>
          Choose a category:

        </label>

        <select
        id='category'
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        className='px-4 py-2 border-gray-300 rounded'
        >
        
        <option value="Programming">Programming</option>
        <option value="Misc">Misc</option>
        <option value="Dark">Dark</option>
        <option value="Pun">Pun</option>
        <option value="Christmas">Christmas</option>
        <option value="Spooky">Spooky</option>

        </select>
      </div>

      <div className="bg-white shadow-lg rounded-lg p-6 max-w-xl w-full text-center mb-4 min-h-[100px] flex items-center justify-center">

        {loading ? (
           <Spinner />
        ) :error ? (
          <p className='text-red-500'>{error}</p>
        ) : (
          <p className='text-lg'>{joke}</p>
        
        )}

     
      </div>

      <div className="flex space-x-4">

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

      <button 
      onClick={saveToFavorites}
      disabled={loading || joke === "Click the buton to get a joke!"}
      className='px-6 py-2 bg-green-500 hover:bg-green-600 text-white rounded transition'
      >
        Save to Favorites
      </button>

      </div>

      {favorites.length > 0 && (
        <div className='mt-8 w-full max-w-xl'>
        <h2 className='text-xl font-semibold mb-2'> Your Favorite jokes</h2>
        <ul className='bg-white shadow rounded p-4 space-y-2'>
          {favorites.map((fav, idx) => (
            <li key={idx} 
            className='border-b pb-2 last:border-b-0 flex justify-between items-center'>

              <span className='text-sm text-left'>
              {fav}
              </span>

              <button onClick={() => handleRemove(fav)}
              className='text-red-500 hover:underline text-xs'
              title='Remove Joke'
              >
                🗑️
              </button>
              
            </li>
          ))}
        </ul>
        </div>
        
      )}

      <button
      onClick={() => {
        setFavorites([]);
        showToast("Favorites Cleared");

      }}
      className='mt-4 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded text-sm'
      >
        Clear All Favorites
      </button>
      
    </div>
  );
}

export default App;