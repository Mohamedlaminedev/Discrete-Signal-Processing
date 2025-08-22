# 🎧 Voice Echo Modulator

A small Python project that lets you record your voice, apply a custom echo-based modulation effect using your own logic, and visualize the results.

---

## 🚀 Features

- 🎤 Records 2 seconds of audio from your microphone
- 🔁 Applies an echo effect by blending the original with a quieter version
- 🎛️ Uses a custom `modulate()` function you create yourself
- 📈 Visualizes original and modulated audio waveforms using Matplotlib
- 🧪 Basic silence detection to avoid processing empty input

---

## 📦 Requirements

Install the dependencies using pip:

```bash
pip install sounddevice numpy matplotlib
