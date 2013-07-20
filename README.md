Airduino
========

An Arduino based rotating model airplane which runs according to a given flight
path. The user sends an SMS with the flight number to a web service. This then
watches for flight take off and sends an SMS to the Airduino to drive the motor.
When the plane lands the motor is switched off. Thus the owner of the Airduino
can monitor when his/her relative are in the air.


Developing: Google AppEngine
----------------------------
Airduino is a Google AppEngine Python application so you will need the SDK from
[here](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python).

When you have made your changes, update the version number in `app.yaml` so
that you can roll back in the AppEngine console if necessary and then run the
following command from the root of your cloned repository:

    <path-to-google_appengine-sdk>/appcfg.py --oauth2 update .


Developing: Arduino
-------------------
Airduino was developed with the
[Arduino GSM shield](http://arduino.cc/en/Main/ArduinoGSMShield).

A tutorial of receiving SMS messages with the GSM library is
[here](http://arduino.cc/en/Tutorial/GSMExamplesReceiveSMS).

If you are using an Arduino Leonardo or Mega, there are extra considerations
about connecting the GSM shield that you need to pay close attention to. Make
sure to follow the instructions
[here](http://arduino.cc/en/Guide/GSMShieldLeonardoMega).

