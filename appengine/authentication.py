#!/usr/bin/env python

import logging
import functools
from google.appengine.api import users

def authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return None

        if not users.is_current_user_admin():
            logging.warn("Blocked authenticated request by %s." % user.email())
            return self.redirect(users.create_logout_url("/"))

        logging.info("Authenticated request by %s." % user.email())

        return method(self, *args, **kwargs)

    return wrapper
