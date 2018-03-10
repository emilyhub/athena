# Get directions without data/wifi/storage
### Created during AthenaHacks 2018 & won Best Daily Use hack

#### Usage
A user without data, or wifi, or storage (aside from storage needed to view texts) can text a number owned by Twilio to get directions
to their destination.
Twilio will fetch the directions and text back with step-by-step directions and a map. Users only need cell service. Can be helpful for
those lost in the woods/grandmas with flip phones/people traveling to a different country.

#### Tools
Flask, Twilio API, Google Maps API

#### Code
Bulk of the code in TwilioMap.py, Googlemaps_image_API.py, GoogleImages.py, and Location.py
Repo also contains remnants of a similar, primitive idea of an app that would allow users to watch videos/listen to music only using cell service.
