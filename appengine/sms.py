import logging

from main import authenticated
import webapp2

class SMSArduinoHandler(webapp2.RequestHandler):
    """SMS the Arduino"""

    @authenticated
    def get(self):
        on = self.request.get('on') == 'on'
        logging.info("SMS Arduino: %s" % on)

        self.redirect('/')

class SMSAppEngineHandler(webapp2.RequestHandler):
    """SMS the AppEngine"""

    @authenticated
    def get(self):
        flight = self.request.get('flight')
        logging.info("SMS AppEngine: %s" % flight)

        self.redirect('/')


application = webapp2.WSGIApplication([
    ('/sms/arduino', SMSArduinoHandler),
    ('/sms/appengine', SMSAppEngineHandler)
], debug=True)
