#cloud.google.com/appengine/docs/standard/go/building-app
#ngrok
from flask import Flask, request, redirect
from twilio.rest import Client
import UserInput

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None) #type is string
    print(body)
    messageTuple = UserInput.Sentence_To_Words(body)
    
    r = MessagingResponse()
    r.message('{}'.format(messageTuple))
    return str(r)


if __name__ == "__main__":
    app.run(debug=True)
