from emotiondetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase): 
    def test_emotion_joy(self): 
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened') 
        self.assertEqual(result_1, 'joy') 
        
    def test_emotion_anger(self):    
        # Test case for anger 
        result_2 = emotion_detector('I am really mad about this') 
        self.assertEqual(result_2, 'anger')

    def test_emotion_disgust(self):
        # Test case for disgust 
        result_3 = emotion_detector('I feel disgusted just hearing about this') 
        self.assertEqual(result_3, 'disgust')

    def test_emotion_sadness(self):
        # Test case for sadness  
        result_4 = emotion_detector('I am so sad about this') 
        self.assertEqual(result_4, 'sadness')

    def test_emotion_fear(self):
        # Test case for fear 
        result_5 = emotion_detector('I am really afraid that this will happen') 
        self.assertEqual(result_5, 'fear')

unittest.main()