import React, {useEffect, useRef, useState} from 'react';
import './App.css';
import ColorPicker from '@rc-component/color-picker';
import '@rc-component/color-picker/assets/index.css';

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

    const customLed = (value: string) => {
        setTimeout(() => {
            fetch("http://192.168.88.103:5000/api/color-picker", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ color: value }),
            })
                .then((res) => res.json());
        }, 1000); // 500ms Pause
    };

  return (
    <div className="App">
        <ColorPicker onChange={(value) => {customLed(value.toRgbString())}}/>
        <button onClick={ledOff}>Off</button>
        <button onClick={ledRed}>Rot</button>
        <button onClick={ledBlue}>Blau</button>
        <button onClick={ledGreen}>Grün</button>
    </div>
  );
}

export default App;
