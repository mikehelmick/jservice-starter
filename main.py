import logging
import os
import jinja2
import webapp2
import json
import urllib2

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

class MainPage(webapp2.RequestHandler):
    def get(self):
        answer = 'answer'
        question = 'question'
        category = 'category'

        template = jinja_environment.get_template('main.html')
        variables = {'answer': answer,
                     'question': question,
                     'category': category}
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
