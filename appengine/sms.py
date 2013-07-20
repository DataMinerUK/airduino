import logging

from main import authenticated
import webapp2

from twilio.rest import TwilioRestClient
from datastore import *

class SMSArduinoHandler(webapp2.RequestHandler):
    """SMS the Arduino"""

    @authenticated
    def post(self):
        on = self.request.get('on') == 'on'
        logging.info("SMS Arduino: %s" % on)
        if on:
          send_sms(get_arduino_phone_number(), "ON")
        else:
          send_sms(get_arduino_phone_number(), "OFF")

        self.redirect('/')

class SMSAppEngineHandler(webapp2.RequestHandler):
    """SMS the AppEngine"""

    @authenticated
    def post(self):
        flight = self.request.get('flight')
        logging.info("SMS AppEngine: %s" % flight)
        send_sms(get_appengine_phone_number, flight)

        self.redirect('/')


def send_sms(to, message):
    client = TwilioRestClient(get_twilio_sid(), get_twilio_token())

    logging.info("Sending SMS to: %s" % to)
    logging.info("Sending SMS from: %s" % get_appengine_phone_number())
    logging.info("Sending SMS message: %s" % message)

    rv = client.sms.messages.create(
      to = to,
      from_ = get_appengine_phone_number(),
      body = message
    )

    logging.info("Twilio response: %s" % rv)



application = webapp2.WSGIApplication([
    ('/sms/arduino', SMSArduinoHandler),
    ('/sms/appengine', SMSAppEngineHandler)
], debug=True)
