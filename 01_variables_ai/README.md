# 🤖 Jarvis v0.1 - AI Command Terminal

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Day_1_Complete-green)
![AI Concepts](https://img.shields.io/badge/AI-Rule_Based-orange)

## 📖 Project Overview
**Jarvis v0.1** is a foundational AI command-line interface (CLI) built to demonstrate core Python logic integrated with basic artificial intelligence concepts.

Unlike standard "Hello World" scripts, this project implements **context-awareness**, **data normalization**, and **predictive logic** to simulate a rudimentary digital assistant.

## 🏗️ Architecture & Logic
The system operates on a linear pipeline:
1.  **Sensory Input**: Captures raw user data via terminal.
2.  **Preprocessing Engine**: Sanitizes inputs (stripping, case normalization) to prevent logic errors.
3.  **Core Processing**:
    * *Identity Management*: Merges static system state with dynamic user context.
    * *Predictive Calculation*: Estimates task completion time using weighted variables.
4.  **Output Generation**: Renders formatted, human-readable intelligence reports.

## 📂 Project Structure
```text
python-ai-learning/
│
├── 01_variables_ai/
│   ├── jarvis.py        # Main executable script
│   └── README.md        # Documentation
│
└── README.md            # Root documentation