import logging
from google.appengine.ext import db


class Configuration(db.Model):
    arduino_phone_number = db.StringProperty()
    appengine_phone_number = db.StringProperty()
    twilio_sid = db.StringProperty()
    twilio_token = db.StringProperty()

def get_configuration():
    existing = Configuration.all().fetch(1)
    if len(existing) == 0:
        return Configuration(
            arduino_phone_number = "",
            appengine_phone_number = "",
            twilio_sid = "",
            twilio_token = ""
        )

    return existing[0]

def set_arduino_phone_number(arduino_phone_number):
    configuration = get_configuration()
    logging.info("Writing Arduino Phone Number to datastore: %s" % arduino_phone_number)
    configuration.arduino_phone_number = arduino_phone_number
    configuration.put()

def get_arduino_phone_number():
    return get_configuration().arduino_phone_number

def set_appengine_phone_number(appengine_phone_number):
    configuration = get_configuration()
    logging.info("Writing AppEngine Phone Number to datastore: %s" % appengine_phone_number)
    configuration.appengine_phone_number = appengine_phone_number
    configuration.put()

def get_appengine_phone_number():
    return get_configuration().appengine_phone_number

def set_twilio_sid(twilio_sid):
    configuration = get_configuration()
    logging.info("Writing Twilio Application SID to datastore: %s" % twilio_sid)
    configuration.twilio_sid = twilio_sid
    configuration.put()

def get_twilio_sid():
    return get_configuration().twilio_sid

def set_twilio_token(twilio_token):
    configuration = get_configuration()
    logging.info("Writing Twilio Authentication Token to datastore: %s" % twilio_token)
    configuration.twilio_token = twilio_token
    configuration.put()

def get_twilio_token():
    return get_configuration().twilio_token
