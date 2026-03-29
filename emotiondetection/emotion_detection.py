import requests # Import the requests library to handle HTTP requests
import json

def get_dominant_emotion(emotion_dict):
    return max(emotion_dict, key=emotion_dict.get)

def print_emotions(emotion_dict):
    for key, value in emotion_dict.items():
        print(key, ":", value)

    
def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse) 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion analysis service 
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 

    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    # Extracting relevant data from the response 
    data = formatted_response['emotionPredictions'][0]
    emotionlist = data['emotion'] 

    # Determine dominant emotion 
    dominant = get_dominant_emotion(emotionlist)
    emotionlist["dominant emotion"] = dominant

    # Print all emotions and their scores
    print_emotions(emotionlist)

    return dominant