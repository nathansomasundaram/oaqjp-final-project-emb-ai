''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
# Import the emotion_detector function from the package created:
from flask import Flask, render_template, request
from emotiondetection.emotion_detection import emotion_detector, print_emotions

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows dominant emotion. 
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    emotionlist = emotion_detector(text_to_analyze)

    # Prepare emotion list for printing in certain order and format
    response = print_emotions(emotionlist)
    return response

@app.route("/")
def render_index_page():
    ''' This code renders default input page in HTML interface 
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
