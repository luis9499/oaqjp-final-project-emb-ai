"""
Unit Tests for Emotion Detection Module
Tests the emotion_detector function with various inputs
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion detection"""

    def test_emotion_detector_joy(self):
        """Test detection of joy emotion"""
        result = emotion_detector("I am happy and excited about this wonderful day!")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertIn('joy', result)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_sadness(self):
        """Test detection of sadness emotion"""
        result = emotion_detector("I am sad and unhappy about this miserable situation.")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_anger(self):
        """Test detection of anger emotion"""
        result = emotion_detector("I am furious and angry about this terrible thing!")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_fear(self):
        """Test detection of fear emotion"""
        result = emotion_detector("I am afraid and scared of this frightening situation.")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_disgust(self):
        """Test detection of disgust emotion"""
        result = emotion_detector("This is disgusting and repulsive!")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_empty_string(self):
        """Test with empty string input"""
        result = emotion_detector("")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_detector_none_input(self):
        """Test with None input"""
        result = emotion_detector(None)

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_detector_whitespace_only(self):
        """Test with whitespace-only input"""
        result = emotion_detector("   ")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_scores_valid_range(self):
        """Test that emotion scores are in valid range (0-1)"""
        result = emotion_detector("I am happy and excited!")

        # Verify scores are not None and are in valid range
        if result['anger'] is not None:
            self.assertGreaterEqual(result['anger'], 0)
            self.assertLessEqual(result['anger'], 1)
        if result['disgust'] is not None:
            self.assertGreaterEqual(result['disgust'], 0)
            self.assertLessEqual(result['disgust'], 1)
        if result['fear'] is not None:
            self.assertGreaterEqual(result['fear'], 0)
            self.assertLessEqual(result['fear'], 1)
        if result['joy'] is not None:
            self.assertGreaterEqual(result['joy'], 0)
            self.assertLessEqual(result['joy'], 1)
        if result['sadness'] is not None:
            self.assertGreaterEqual(result['sadness'], 0)
            self.assertLessEqual(result['sadness'], 1)

    def test_emotion_detector_mixed_emotions(self):
        """Test text with mixed emotions"""
        result = emotion_detector("I am happy but also a bit sad about the situation.")

        self.assertIsNotNone(result)
        self.assertEqual(result['status_code'], 200)
        self.assertIn('dominant_emotion', result)
        self.assertIsNotNone(result['dominant_emotion'])

    def test_emotion_detector_returns_all_emotions(self):
        """Test that result contains all emotion fields"""
        result = emotion_detector("Test text")

        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        self.assertIn('status_code', result)


if __name__ == '__main__':
    unittest.main()
