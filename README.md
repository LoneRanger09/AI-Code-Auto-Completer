# AI-Code-Auto-Completer
# AI Code Auto-Completer 🤖⌨️  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An intelligent code auto-completion tool built using **CodeT5** model. This project provides a simple frontend interface for developers to input partial code snippets and get smart completions in real-time using a FastAPI backend.

---
## ✨ Features

- **Context-Aware Suggestions** - Understands your code context for accurate completions
- **Multi-Language Support** - Works with Python, JavaScript, Java, C++, and more
- **Lightning Fast** - Optimized for minimal latency during development
- **Personalized Learning** - Adapts to your coding style over time
- **Editor Agnostic** - Compatible with VSCode, PyCharm, Vim, and others

## 📁 Project Structure
```bash
ai-code-autocompleter/
├── backend/ │
├── main.py # FastAPI server code │
├── requirements.txt # Python dependencies
│
├── frontend/ │
├── index.html # Frontend UI │
├── style.css # (Optional) Styling for UI │
└── script.js # JavaScript to call backend
├── setup.sh # Shell script to set up environment
└── README.md # Project documentation
```

---

## 🧰 Tech Stack

### 🔙 Backend
- **FastAPI** – API server
- **Transformers** (Hugging Face) – Pretrained CodeT5 model
- **Uvicorn** – ASGI server
- **Pydantic** – For request validation
- **CORS Middleware** – For cross-origin communication

### 🔜 Frontend
- **HTML/CSS** – Basic user interface
- **JavaScript (Fetch API)** – To send requests to backend

---

## 🚀 How to Run the Project

### 📦 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-code-autocompleter.git
cd ai-code-autocompleter
```
## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Quick Install
```bash
pip install ai-code-autocompleter
```
```bash
git clone https://github.com/yourusername/ai-code-autocompleter.git
cd ai-code-autocompleter
pip install -e ".[dev]"
```
