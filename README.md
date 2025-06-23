# 🖐️ Hand Gesture Calculator using MediaPipe

This is a Python-based calculator that uses **hand gestures** for performing basic arithmetic operations — all without any physical contact! Built with [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/), the calculator detects fingers in real-time and interprets them as input digits and operators.

---

## 🎯 Features

- 🔢 Recognize digits (0–9) using finger gestures  
- ➕➖✖️➗ Perform basic operations: addition, subtraction, multiplication, division  
- 🖥️ Real-time video processing with OpenCV  
- ✋ Touchless interface for fun and practical experimentation

---

## 🛠️ Tech Stack

- **Python**
- **MediaPipe** (for hand tracking)
- **OpenCV** (for video capture & display)
- **NumPy**

---

## 🚀 How It Works

1. The camera captures hand gestures in real time.
2. MediaPipe tracks hand landmarks (like fingertips).
3. Finger positions are analyzed to recognize digits or operators.
4. The recognized inputs are used to perform calculations.
5. The result is displayed on screen.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/hand-gesture-calculator.git
cd hand-gesture-calculator
pip install -r requirements.txt
python calculator.py
