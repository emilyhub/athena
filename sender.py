from flask import Flask, request

from twilio.twiml.messaging_response import Redirect, MessagingResponse
#from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/mms', methods=['GET','POST'])
def mms():
    number = request.form['From']
    client_message = request.form['Body']
    
    #start out TwiML response
    response = MessagingResponse()
    
    #add a text message
    msg = response.message(f'Hello, {number}! you entered {client_message}')
    #add a youtube message
    msg.media('https://www.wallpaperbackgrounds.org/wp-content/uploads/Picture.jpg')
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)