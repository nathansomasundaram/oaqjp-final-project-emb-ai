import requests # Import the requests library to handle HTTP requests
import json

def get_dominant_emotion(emotion_dict):
    return max(emotion_dict, key=emotion_dict.get)

''' This code receives the emotion list from the HTML interface and 
        formats the text to be printed in a pre-defined format.
'''
def print_emotions(emotion_dict):
    allemotions = ""
    for key, value in emotion_dict.items():
        if (key == "dominant_emotion") :
            currentemotion = ". The dominant emotion is " + str(value) + ". "
        else : 
            currentemotion = "'" + key + "':" + str(value) + " "
        allemotions = allemotions + currentemotion    
    return allemotions

def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse) 
    # Handle empty input
    if not text_to_analyse.strip():
        data = {"Error" : "Pleaseenter input"}
        return data

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion analysis service 
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 

    # Handle http 400 response 
    if (response.status_code == 400) :
        data = {'anger': 'None', 'disgust': 'None', 'fear': 'None', 'joy': 'None', 'sadness': 'None','dominant_emotion':'None'}
        return data
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting relevant data from the response 
    data = formatted_response['emotionPredictions'][0]
    emotionlist = data['emotion'] 

    # Determine dominant emotion 
    dominant = get_dominant_emotion(emotionlist)
    emotionlist["dominant_emotion"] = dominant

    return emotionlist