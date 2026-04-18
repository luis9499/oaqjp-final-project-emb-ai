# Emotion Detection - Final Project

A comprehensive AI-powered web application that detects emotions in text using Watson NLP and Flask.

## 📋 Project Overview

This project implements an emotion detection system that analyzes text and identifies emotional content. The application provides:

- **Emotion Analysis**: Detects five emotions: joy, sadness, anger, fear, and disgust
- **Web Interface**: User-friendly web application built with Flask
- **API Endpoint**: RESTful API for emotion detection
- **Error Handling**: Comprehensive error handling for invalid inputs
- **Unit Tests**: Complete test suite with 11 test cases
- **Code Quality**: Static code analysis with pylint achieving 10.00/10 score

## 🎯 Project Tasks

### Task 1: Repository Setup ✓
- GitHub repository configured
- Project README with comprehensive documentation

### Task 2: Emotion Detection Module ✓
- Created `emotion_detection.py` with Watson NLP integration
- Fallback local emotion detection using keyword-based approach
- Support for 5 emotion categories

### Task 3: Output Formatting ✓
- Structured JSON response format
- Consistent output with emotion scores (0-1) and dominant emotion
- Clear and organized data structure

### Task 4: Package Validation ✓
- Created `__init__.py` for EmotionDetection package
- Package properly exports emotion_detector function
- Successfully validates as Python package

### Task 5: Unit Testing ✓
- 11 comprehensive unit tests
- 100% test success rate
- Tests cover all emotions, edge cases, and response structure

### Task 6: Flask Web Deployment ✓
- Created `server.py` with Flask web server
- Responsive HTML interface with modern design
- Real-time emotion detection via API

### Task 7: Error Handling ✓
- Returns status code 400 for invalid input
- Graceful handling of empty/whitespace text
- Error messages in API responses
- Form validation in web interface

### Task 8: Static Code Analysis ✓
- Pylint configuration for code quality
- Perfect score: 10.00/10
- High quality code standards

## 📂 Project Structure

```
PROYECTO_FINAL_DETECTOR_EMOCIONES/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
├── requirements.txt
├── README.md
├── 2a_emotion_detection.py
├── 2b_application_creation.txt
├── 3a_output_formatting.py
├── 3b_formatted_output_test.txt
├── 4b_packaging_test.txt
├── 5a_unit_testing.py
├── 5b_unit_testing_result.txt
├── 6a_server.py
├── 7a_error_handling_function.py
├── 7b_error_handling_server.py
├── 8a_server_modified.py
├── 8b_static_code_analysis.txt
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd PROYECTO_FINAL_DETECTOR_EMOCIONES
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Start the Web Server:
```bash
python server.py
```

Access at http://localhost:5000

#### Run Unit Tests:
```bash
python -m unittest test_emotion_detection.py -v
```

#### Run Static Code Analysis:
```bash
pylint --disable=C0114,C0116 EmotionDetection/emotion_detection.py server.py
```

## 🔧 API Documentation

### Endpoint: POST /emotion_detector

**Request:**
```json
{
    "text": "I am happy and excited about this wonderful day!"
}
```

**Success Response (200):**
```json
{
    "emotions": {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 1.0,
        "sadness": 0.0
    },
    "dominant_emotion": "joy"
}
```

**Error Response (400):**
```json
{
    "error": "Invalid input. Please enter some text."
}
```

## 📊 Emotion Categories

- **Joy**: Happiness, excitement, pleasure, contentment
- **Sadness**: Sorrow, unhappiness, grief, depression
- **Anger**: Rage, frustration, annoyance, hostility
- **Fear**: Anxiety, worry, panic, dread
- **Disgust**: Revulsion, repulsion, contempt, aversion

## 🧪 Testing

The project includes 11 comprehensive unit tests:

```bash
python -m unittest test_emotion_detection.py -v
```

**Test Coverage:**
- ✓ Joy emotion detection
- ✓ Sadness emotion detection
- ✓ Anger emotion detection
- ✓ Fear emotion detection
- ✓ Disgust emotion detection
- ✓ Empty string handling
- ✓ None input handling
- ✓ Whitespace-only handling
- ✓ Score range validation
- ✓ Mixed emotions
- ✓ Response structure validation

## 📈 Code Quality

Static code analysis ensures professional code standards:

```bash
pylint --disable=C0114,C0116 EmotionDetection/emotion_detection.py server.py
```

**Result: 10.00/10** ✓

## 🛠️ Technologies Used

- **Python 3**: Programming language
- **Flask**: Web framework
- **Watson NLP**: IBM's Natural Language Understanding
- **unittest**: Python's built-in testing framework
- **pylint**: Code quality analysis

## 📝 Features

### Web Interface
- Clean, modern UI with gradient design
- Real-time emotion analysis
- Visual emotion score display
- Error messaging
- Responsive design

### API Features
- RESTful endpoint for programmatic access
- JSON request/response format
- Comprehensive error handling
- HTTP status codes (200, 400, 500)

### Error Handling
- Empty text validation
- None input handling
- Whitespace trimming
- User-friendly error messages
- HTTP status codes

## 📦 Dependencies

- Flask >= 2.0.0
- requests >= 2.28.0
- pylint >= 2.15.0

## 🎓 Educational Project

This project demonstrates:
- Full-stack web development with Flask
- Natural Language Processing integration
- Comprehensive error handling
- Unit testing and quality assurance
- Static code analysis
- RESTful API design
- Modern web interfaces

---

**Version:** 1.0.0
**Last Updated:** April 18, 2026
