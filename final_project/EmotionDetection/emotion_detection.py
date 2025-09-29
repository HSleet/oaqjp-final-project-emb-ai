import requests  
import json

def emotion_detector(text_to_analyse):
    # Set up required params for the emotion detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Get thte response from the NLP library
    response = requests.post(url, json = myobj, headers=header)

    # Format the response into a json
    formatted_response = json.loads(response.text)

    # Handle invalid 400 responses
    if response.status_code == 400:
        emotions_dict = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    elif response.status_code == 200:
        # Extract the emotions from the response
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']

        # Find the highest scored emotion
        dominant_emotion = ''
        max_val = 0
        for key,value in emotions_dict.items():
            if value > max_val:
                max_val = value
                dominant_emotion = key
        
        # Add the dominant emotion to the response dictionary
        emotions_dict['dominant_emotion'] = dominant_emotion

    return emotions_dict
