"""
Flask Web Server for Emotion Detection Application
ERROR HANDLING - BLANK INPUT VALIDATION (Tarea 7 - Actividad 2)
"""

from flask import Flask, request, jsonify, render_template_string
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    API endpoint for emotion detection with blank input error handling.
    
    Query parameter: text - The text to analyze
    Returns emotion scores and dominant emotion.
    Returns 400 status if text is empty or invalid.
    """

    # ERROR HANDLING: Get text from query parameters
    text = request.args.get('text', '').strip()

    # ERROR HANDLING: Check for empty or blank input - Returns 400
    if not text:
        return jsonify({
            'error': 'Invalid input. Please enter some text.'
        }), 400

    # Get emotion detection results
    result = emotion_detector(text)

    # ERROR HANDLING: Check if emotion detector returned error status
    if result.get('status_code') == 400:
        return jsonify({
            'error': 'Invalid input. Please enter some text.'
        }), 400

    # Extract results
    emotions = {
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness']
    }

    # SUCCESS: Return 200 with emotion results
    return jsonify({
        'emotions': emotions,
        'dominant_emotion': result['dominant_emotion']
    }), 200


@app.errorhandler(404)
def page_not_found(_error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def internal_error(_error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500
