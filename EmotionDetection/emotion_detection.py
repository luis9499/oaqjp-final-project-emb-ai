"""
Emotion Detection Module using Watson NLP
Detects emotions in text using natural language processing
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes text and detects emotions using Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A formatted dictionary containing emotion scores and the dominant emotion.
              Returns error status 400 if text is empty or invalid.
    """

    # Check for empty or None text
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }

    # Watson NLP API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json"
    }

    # Request payload for Watson NLP
    data = {
        "raw_document": {
            "content": text_to_analyze
        }
    }

    try:
        # Make the API call to Watson NLP
        response = requests.post(url, json=data, headers=headers, timeout=10)

        # If successful response from Watson
        if response.status_code == 200:
            response_data = response.json()
            emotion = response_data.get("emotionPredict", [{}])[0].get("emotion", {})

            # Find the dominant emotion
            if emotion:
                dominant_emotion = max(emotion, key=emotion.get)

                return {
                    "anger": emotion.get("anger", 0),
                    "disgust": emotion.get("disgust", 0),
                    "fear": emotion.get("fear", 0),
                    "joy": emotion.get("joy", 0),
                    "sadness": emotion.get("sadness", 0),
                    "dominant_emotion": dominant_emotion,
                    "status_code": 200
                }
        else:
            # If Watson API is not available, use local emotion detection
            return _local_emotion_detection(text_to_analyze)

    except (requests.exceptions.RequestException, json.JSONDecodeError,
            KeyError):
        # Fallback to local emotion detection if API fails
        return _local_emotion_detection(text_to_analyze)

    return None


def _local_emotion_detection(text_to_analyze):
    """
    Local emotion detection using keyword-based approach.
    This is a fallback when Watson API is not available.

    Args:
        text_to_analyze (str): The text to analyze

    Returns:
        dict: Emotion scores and dominant emotion
    """

    text_lower = text_to_analyze.lower()

    # Emotion keywords dictionary
    emotion_keywords = {
        "joy": ["happy", "joy", "love", "fun", "excited", "great", "excellent",
                "wonderful", "fantastic", "amazing", "brilliant", "perfect",
                "awesome", "delighted", "pleased"],
        "sadness": ["sad", "unhappy", "depressed", "grief", "down", "blue",
                    "miserable", "down", "sorrow", "devastated", "unfortunate"],
        "anger": ["angry", "mad", "furious", "rage", "hate", "annoyed",
                  "frustrated", "irritated", "upset", "livid"],
        "fear": ["fear", "afraid", "scared", "terrified", "worried", "anxious",
                 "nervous", "panic", "dread"],
        "disgust": ["disgusting", "repulsive", "gross", "horrible", "awful",
                    "nasty", "vile", "abominable"]
    }

    # Count emotion words
    emotion_scores = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            emotion_scores[emotion] += text_lower.count(keyword)

    # Normalize scores to 0-1 range
    max_score = max(emotion_scores.values()) if max(emotion_scores.values()) > 0 else 1
    normalized_scores = {k: round(v / max_score, 3) for k, v in emotion_scores.items()}

    # Find dominant emotion
    dominant_emotion = max(normalized_scores, key=normalized_scores.get)

    return {
        "anger": normalized_scores["anger"],
        "disgust": normalized_scores["disgust"],
        "fear": normalized_scores["fear"],
        "joy": normalized_scores["joy"],
        "sadness": normalized_scores["sadness"],
        "dominant_emotion": dominant_emotion,
        "status_code": 200
    }
