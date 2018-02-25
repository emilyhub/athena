#cloud.google.com/appengine/docs/standard/go/building-app
#ngrok
#blob storage
from flask import Flask, request, redirect
from twilio.rest import Client
import Googlemaps_image_API
import GoogleImages

#my google static map key = AIzaSyCVReYL_jNGToQ1obg-AN31KCu6XMq5XAI
#https://maps.googleapis.com/maps/api/staticmap?center=0,0&zoom=1&size=100x100&key=AIzaSyCVReYL_jNGToQ1obg-AN31KCu6XMq5XAI



from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    
    #r.message("Hi! Please enter addresses of your location and your destination\n in this format: \nStarting Location\n Destination\n")
        
    r2 = MessagingResponse()
    
    body = request.values.get('Body', None) #type is string
    current_location = body.split('\n')[0]
    image_url = GoogleImages.build_directions_url(current_location)
    
    r2.message("Getting your directions...")
    
    locations = body.split('\n')
    print(locations)
    url = Googlemaps_image_API.build_directions_url(locations)
    json_dict = Googlemaps_image_API.get_dict(url)
    
    r2.message(Googlemaps_image_API.output(json_dict))
    
    msg = r2.message()
    msg.media(image_url)

    
    
#     r.message("Sending video...")
#     msg = r.message(body)
#     msg.media("https://annaq1.blob.core.windows.net/asset-9d53dc63-cdb9-4480-bf15-4d88bf698803/Funny%20Dogs%20-%20A%20Funny%20Dog%20Videos%20Compilation%202015.mp4?sv=2015-07-08&sr=c&si=e9b297b4-8c05-4249-adda-77678de82dda&sig=ROjCELgcy5%2BgTIirO1%2F29%2BZ1Fjg%2F%2BBlFI1sYCW0elUk%3D&st=2018-02-25T07%3A42%3A42Z&se=2118-02-25T07%3A42%3A42Z")
#     r.message("Sent")
    return str(r2)


if __name__ == "__main__":
    app.run(debug=True)