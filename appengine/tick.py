import logging

import webapp2

class TickHandler():
    """Tick"""

    logging.info("Tick")


application = webapp2.WSGIApplication([('/tick', TickHandler)], debug=True)
