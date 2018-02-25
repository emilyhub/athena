#cloud.google.com/appengine/docs/standard/go/building-app
#ngrok
from flask import Flask
from twilio.rest import Client

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    r = MessagingResponse()
    r.message('Hello World')
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)
