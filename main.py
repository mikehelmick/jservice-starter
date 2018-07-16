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
        response = urllib2.urlopen('http://jservice.io/api/random')
        content = response.read()
        content_dict = json.loads(content)

        answer = content_dict[0]['answer']
        question = content_dict[0]['question']
        category = content_dict[0]['category']['title']

        template = jinja_environment.get_template('main.html')
        variables = {'answer': answer,
                     'question': question,
                     'category': category}
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
