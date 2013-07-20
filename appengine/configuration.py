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

class ConfigurationTwilioKeyHandler(webapp2.RequestHandler):
    """Set the Twilio Key"""

    @authenticated
    def post(self):
        key = self.request.get('key')
        logging.info("Set Twilio Key: %s" % key)
        set_twilio_key(key)

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
    ('/configuration/twilio/key', ConfigurationTwilioKeyHandler),
    ('/configuration/appengine/phonenumber', ConfigurationAppEnginePhoneNumberHandler)
], debug=True)
