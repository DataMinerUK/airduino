import logging

import webapp2


class TickHandler(webapp2.RequestHandler):

    def get(self):
        """Tick"""

        logging.info("Tick")


application = webapp2.WSGIApplication([('/tick', TickHandler)], debug=True)
