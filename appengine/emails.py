import logging

from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

import webapp2
import email

from model import *

class ReceiveEmail(InboundMailHandler):
    """Receive a flight code by email."""

    def receive(self, message):
        user = user_from_email(email.utils.parseaddr(message.sender)[1])
        for content_type, body in message.bodies('text/plain'):
            # http://stackoverflow.com/questions/4021392/how-do-you-decode-a-binary-encoded-mail-message-in-python
            if body.encoding == '8bit':
                body.encoding = '7bit'
            content = body.decode()

            content = content.strip()

            flight = content.split('\n')[0].strip()


application = webapp2.WSGIApplication([ReceiveEmail.mapping()], debug=True)
