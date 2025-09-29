"""
Server file to run the flask app.
This file contains the routes and functions to handle requests and responses.
It uses the emotion_detector function from the emotion_detection module to get the emotions from the text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")


@app.route("/emotionDetector")
def emotion_detect():
    """
    Function to detect the emotion from the given text using Watson NLP API.
    
    Returns:
    str: The response from the API.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if not response['dominant_emotion']:
        text = "Invalid text! please try again!"
    else:
        text = f"For the given statement, the system response is 'anger': {response['anger']},\
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness':\
        {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return text


@app.route("/")
def render_index_page():
    """Rendering page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
