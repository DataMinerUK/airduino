#!/usr/bin/env python

import os
import logging
import functools

from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2

from datastore import *


from authentication import authenticated

class BaseHandler(webapp2.RequestHandler):
    def render(self, template_name, template_values):
        path = os.path.join(os.path.dirname(__file__), 'templates/%s.html' % template_name)
        body = template.render(path, template_values)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(body)


class MainHandler(BaseHandler):
    """Show the control panel."""

    @authenticated
    def get(self):
        self.render('index', {
            'current_user': users.get_current_user(),
            'configuration': get_configuration(),
            'logout': users.create_logout_url("/")
        })


application = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

