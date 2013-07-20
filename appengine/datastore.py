import logging
from google.appengine.ext import db


class Configuration(db.Model):
    arduino_phone_number = db.StringProperty()
    appengine_phone_number = db.StringProperty()
    twilio_key = db.StringProperty()

def get_configuration():
    existing = Configuration.all().fetch(1)
    if len(existing) == 0:
        return Configuration(
            arduino_phone_number = "",
            appengine_phone_number = "",
            twilio_key = ""
        )

    return existing[0]

def set_arduino_phone_number(arduino_phone_number):
    configuration = get_configuration()
    logging.info("Writing Arduino Phone Number to datastore: %s" % arduino_phone_number)
    configuration.arduino_phone_number = arduino_phone_number
    configuration.put()

def set_appengine_phone_number(appengine_phone_number):
    configuration = get_configuration()
    configuration.appengine_phone_number = appengine_phone_number
    configuration.put()

def set_twilio_key(twilio_key):
    configuration = get_configuration()
    configuration.twilio_key = twilio_key
    configuration.put()