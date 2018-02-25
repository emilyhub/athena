#cloud.google.com/appengine/docs/standard/go/building-app
#ngrok
#blob storage
from flask import Flask, request, redirect
from twilio.rest import Client
#import UserInput
import start

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None) #type is string
    print(body)
    video = start.download_video(body)
    #messageTuple = UserInput.Sentence_To_Words(body)
    
    r = MessagingResponse()
    r.message("Sending video...")
    msg = r.message(body)
    msg.media("https://annaq1.blob.core.windows.net/asset-9d53dc63-cdb9-4480-bf15-4d88bf698803/Funny%20Dogs%20-%20A%20Funny%20Dog%20Videos%20Compilation%202015.mp4?sv=2015-07-08&sr=c&si=e9b297b4-8c05-4249-adda-77678de82dda&sig=ROjCELgcy5%2BgTIirO1%2F29%2BZ1Fjg%2F%2BBlFI1sYCW0elUk%3D&st=2018-02-25T07%3A42%3A42Z&se=2118-02-25T07%3A42%3A42Z")
    r.message("Sent")
    return str(r)


if __name__ == "__main__":
    app.run(debug=True)
