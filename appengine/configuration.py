import logging

from main import authenticated
from datastore import *
import webapp2
import time

class ConfigurationArduinoPhoneNumberHandler(webapp2.RequestHandler):
    """Set the Arduino Phone Number"""

    @authenticated
    def post(self):
        phone_number = self.request.get('phonenumber')
        logging.info("Set Arduino Phone Number: %s" % phone_number)
        set_arduino_phone_number(phone_number)

        time.sleep(1)
        self.redirect('/')

class ConfigurationTwilioSIDHandler(webapp2.RequestHandler):
    """Set the Twilio Application SID"""

    @authenticated
    def post(self):
        sid = self.request.get('sid')
        logging.info("Set Twilio Application SID: %s" % sid)
        set_twilio_sid(sid)

        time.sleep(1)
        self.redirect('/')

class ConfigurationTwilioTokenHandler(webapp2.RequestHandler):
    """Set the Twilio Authentication Token"""

    @authenticated
    def post(self):
        token = self.request.get('token')
        logging.info("Set Twilio Authentication Token: %s" % token)
        set_twilio_token(token)

        time.sleep(1)
        self.redirect('/')

class ConfigurationAppEnginePhoneNumberHandler(webapp2.RequestHandler):
    """Set the AppEngine Phone Number"""

    @authenticated
    def post(self):
        phone_number = self.request.get('phonenumber')
        logging.info("Set AppEngine Phone Number: %s" % phone_number)
        set_appengine_phone_number(phone_number)

        time.sleep(1)
        self.redirect('/')


application = webapp2.WSGIApplication([
    ('/configuration/arduino/phonenumber', ConfigurationArduinoPhoneNumberHandler),
    ('/configuration/twilio/sid', ConfigurationTwilioSIDHandler),
    ('/configuration/twilio/token', ConfigurationTwilioTokenHandler),
    ('/configuration/appengine/phonenumber', ConfigurationAppEnginePhoneNumberHandler)
], debug=True)
