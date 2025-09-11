import React from 'react';
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

    const Fade = () => {
        fetch("http://192.168.88.103:5000/api/led-fade", {
            method: "POST",
        })
            .then((res) => res.json())
    };

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
        }, 500); // 500ms Pause
    };

  return (
    <div className="App">
        <p className={"Text"}>LED Dashboard</p>
        <div className="test">
            <ColorPicker onChange={(value) => {customLed(value.toRgbString())}}/>
        </div>
        <button onClick={ledOff} className={"ledOffButton"}>Off</button>
        <button onClick={Fade} className={"ledFadeButton"}>Fade</button>
    </div>
  );
}

export default App;
