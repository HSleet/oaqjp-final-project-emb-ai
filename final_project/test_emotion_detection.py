from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case 1: Joy emotion
        text = "I am glad this happened"
        expected_emotion = "joy"
        dominant_emotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

        # Test case 2: Anger emotion
        text = "I am really mad about this"
        expected_emotion = "anger"
        dominant_emotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

        # Test case 3: Disgust emotion
        text = "I feel disgusted just hearing about this"
        expected_emotion = "disgust"
        dominant_emotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

        # Test case 4: Sadness emotion
        text = "I am so sad about this"
        expected_emotion = "sadness"
        dominant_emotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

        # Test case 5: Fear emotion
        text = "I am really afraid that this will happen"
        expected_emotion = "fear"
        dominant_emotion = emotion_detector(text)['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)
        

if __name__ == '__main__':
    unittest.main()