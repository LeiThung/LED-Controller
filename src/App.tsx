import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

    const ledOff = () => {
        fetch("http://localhost:5000/api/led-off", {
            method: "POST",
        })
            .then((res) => res.json())
    };

    const ledRed = () => {
        fetch("http://localhost:5000/api/led-red", {
            method: "POST",
        })
            .then((res) => res.json())
    };

  return (
    <div className="App">
        <button onClick={ledOff}>Off</button>
        <button onClick={ledRed}>Rot</button>
        <button>Blau</button>
    </div>
  );
}

export default App;
