import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

    const ledOff = () => {
        fetch("http://192.168.88.103:5000/api/led-off", {
            method: "POST",
        })
            .then((res) => res.json())
    };

    const ledRed = () => {
        fetch("http://192.168.88.103:5000/api/led-red", {
            method: "POST",
        })
            .then((res) => res.json())
    };

    const ledBlue = () => {
        fetch("http://192.168.88.103:5000/api/led-blue", {
            method: "POST",
        })
            .then((res) => res.json())
    }

    const ledGreen = () => {
        fetch("http://192.168.88.103:5000/api/led-green", {
            method: "POST",
        })
            .then((res) => res.json())
    }

  return (
    <div className="App">
        <button onClick={ledOff}>Off</button>
        <button onClick={ledRed}>Rot</button>
        <button onClick={ledBlue}>Blau</button>
        <button onClick={ledGreen}>Grün</button>
    </div>
  );
}

export default App;
