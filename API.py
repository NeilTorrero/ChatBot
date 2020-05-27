import requests
from parse import *
BASE_URL = 'http://www.dnd5eapi.co'
"""
install google-cloud-sdk
cd google-cloud-sdk
./google-cloud-sdk/install.sh
./google-cloud-sdk/bin/gcloud init
gcloud config set accessibility/screen_reader true
export GOOGLE_APPLICATION_CREDENTIALS = 'd-d-otyuot-b3f7caf37164.json'
------------
DIALOGFLOW_PROJECT_ID = 'd-d-otyuot'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = 'd-d-otyuot-b3f7caf37164.json'
SESSION_ID = '123456789'

add to enviroment variables the ggogle_application_credentials
"""

def getInfoAPI(type, name):
    url = BASE_URL + '/api/' + type + '/' + name + '/'
    response = requests.get(url)
    data = response.json()
    print(data)
    print(data['name'])
    print(data['level'])
    print(data['range'])
    print(data['desc'])
    return data

def diceParse(text):
    return(search("{:d}d{:d}",text))

def dialogflow(input_text, chat_id):
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path("d-d-otyuot", chat_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=input_text, language_code="en-US")

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    #print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    #print('Detected intent: {} (confidence: {})\n'.format(
    #    response.query_result.intent.display_name,
    #    response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    #print(response)
    return response
