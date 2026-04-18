"""
Flask Web Server for Emotion Detection Application
STATIC CODE ANALYSIS - HIGH QUALITY CODE (Tarea 8)
"""

from flask import Flask, request, jsonify, render_template_string
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotion Detection Web Application</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }

        h1 {
            color: #333;
            margin-bottom: 10px;
            text-align: center;
            font-size: 28px;
        }

        .subtitle {
            color: #666;
            text-align: center;
            margin-bottom: 30px;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }

        textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            font-family: inherit;
            resize: vertical;
            min-height: 100px;
            transition: border-color 0.3s;
        }

        textarea:focus {
            outline: none;
            border-color: #667eea;
        }

        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        button:active {
            transform: translateY(0);
        }

        .result {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            display: none;
        }

        .result.show {
            display: block;
        }

        .result h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 18px;
        }

        .emotion-scores {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }

        .emotion-item {
            background: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border-left: 4px solid #667eea;
        }

        .emotion-label {
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 5px;
        }

        .emotion-value {
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }

        .dominant-emotion {
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 8px;
            text-align: center;
            font-size: 18px;
            font-weight: 600;
        }

        .error {
            color: #e74c3c;
            padding: 15px;
            background: #fadbd8;
            border-radius: 8px;
            display: none;
            margin-bottom: 20px;
        }

        .error.show {
            display: block;
        }

        .loading {
            display: none;
            text-align: center;
            color: #667eea;
            font-weight: 600;
        }

        .loading.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎭 Emotion Detection</h1>
        <p class="subtitle">Analyze the emotions in your text</p>

        <form id="emotionForm">
            <div class="error" id="errorMessage"></div>
            <div class="form-group">
                <label for="userInput">Enter your text:</label>
                <textarea id="userInput" name="text" placeholder="Type something..."></textarea>
            </div>
            <button type="submit">Analyze Emotions</button>
            <div class="loading" id="loading">Analyzing...</div>
        </form>

        <div class="result" id="result">
            <h3>Results:</h3>
            <div class="emotion-scores" id="emotionScores"></div>
            <div class="dominant-emotion">
                Dominant Emotion: <span id="dominantEmotion"></span>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('emotionForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const text = document.getElementById('userInput').value;
            const errorElement = document.getElementById('errorMessage');
            const resultElement = document.getElementById('result');
            const loadingElement = document.getElementById('loading');

            errorElement.classList.remove('show');
            resultElement.classList.remove('show');
            loadingElement.classList.add('show');

            try {
                const response = await fetch('/emotion_detector', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: text })
                });

                const data = await response.json();
                loadingElement.classList.remove('show');

                if (response.status === 400) {
                    errorElement.textContent = data.error || 'Invalid input. Please enter some text.';
                    errorElement.classList.add('show');
                    return;
                }

                if (response.ok) {
                    const emotions = data.emotions;
                    const dominantEmotion = data.dominant_emotion;

                    const emotionScores = document.getElementById('emotionScores');
                    emotionScores.innerHTML = '';

                    for (const [emotion, score] of Object.entries(emotions)) {
                        const emotionItem = document.createElement('div');
                        emotionItem.className = 'emotion-item';
                        emotionItem.innerHTML = `
                            <div class="emotion-label">${emotion}</div>
                            <div class="emotion-value">${(score * 100).toFixed(1)}%</div>
                        `;
                        emotionScores.appendChild(emotionItem);
                    }

                    document.getElementById('dominantEmotion').textContent = dominantEmotion;
                    resultElement.classList.add('show');
                }
            } catch (error) {
                loadingElement.classList.remove('show');
                errorElement.textContent = 'Error: ' + error.message;
                errorElement.classList.add('show');
            }
        });
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Render the main web interface"""
    return render_template_string(HTML_TEMPLATE)


@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    """
    API endpoint for emotion detection.

    Expects JSON input with 'text' field.
    Returns emotion scores and dominant emotion.
    Returns 400 status if text is empty or invalid.
    """

    # Get JSON data from request
    data = request.get_json()

    # Validate input
    if not data or 'text' not in data:
        return jsonify({
            'error': 'Invalid input. Please provide text field.'
        }), 400

    text = data.get('text', '').strip()

    # Check for empty text
    if not text:
        return jsonify({
            'error': 'Invalid input. Please enter some text.'
        }), 400

    # Get emotion detection results
    result = emotion_detector(text)

    # Check if there was an error in emotion detection
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


if __name__ == '__main__':
    print("🚀 Starting Emotion Detection Web Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    app.run(debug=True, host='localhost', port=5000)
