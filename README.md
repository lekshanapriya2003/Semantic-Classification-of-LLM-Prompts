# Semantic Task Classification of LLM Prompts

## Overview
This project classifies user prompts into one of four categories:
- Coding
- Reasoning
- Summarization
- General

It uses a FastText-based text classification model integrated with a Streamlit web application to provide real-time predictions.

---

## Objective
With the increasing use of Large Language Models (LLMs), prompts vary widely in intent. This project aims to:
- Automatically identify the type of prompt
- Improve prompt understanding
- Enable better downstream processing

---

## Features
- Real-time prompt classification
- Simple and interactive user interface using Streamlit
- Handles multi-line input safely for FastText
- Displays predicted category and score breakdown
- Lightweight and fast inference

---

## Tech Stack
- Language: Python
- Model: FastText
- Framework: Streamlit
- Libraries: pandas

---

## Project Structure
```

Semantic-Task-Classification/
│
├── app.py                          # Main Streamlit application
├── openorca_fasttext_model.bin     # Trained FastText model
├── requirements.txt                # Dependencies
└── README.md                       # Documentation

```

---

## Installation

### 1. Clone the repository
```

git clone [https://github.com/your-username/semantic-task-classification.git](https://github.com/your-username/semantic-task-classification.git)
cd semantic-task-classification

```

### 2. Create virtual environment (optional)
```

python -m venv venv
venv\Scripts\activate

```

### 3. Install dependencies
```

pip install -r requirements.txt

```

---

## Run the Application
```

streamlit run app.py

```

Then open:
```

[http://localhost:8501](http://localhost:8501)

```

---

## Example Prompts

### Coding
```

Write a Python function to reverse a linked list.

```

### Reasoning
```

Explain how binary search works.

```

### Summarization
```

Summarize this paragraph in three points.

```

### General
```

What is the capital of France?

```

---

## How It Works
1. User enters a prompt
2. Input is preprocessed (removal of newlines and normalization)
3. FastText model predicts probabilities for each category
4. The category with the highest score is selected
5. Results are displayed in the UI

---

## Model Details
- Algorithm: FastText
- Input: Text prompt
- Output: Category probabilities
- Categories:
  - coding
  - reasoning
  - summarization
  - general

---

## Limitations
- Accuracy depends on training data quality
- May struggle with ambiguous or mixed-intent prompts
- Limited contextual understanding compared to transformer-based models

---

## Future Improvements
- Use transformer-based models (BERT, LLMs)
- Improve dataset quality and balance
- Add confidence-based visualization
- Support multi-label classification
- Enhance UI and user experience

---

## Conclusion
This project demonstrates a simple and efficient approach to classifying LLM prompts using FastText. It provides a foundation for building more advanced prompt understanding systems.
```

---

If you want a **higher-grade README (with diagrams, architecture section, evaluation metrics)**, say so — what you have now is solid but still basic for top-tier submissions.
