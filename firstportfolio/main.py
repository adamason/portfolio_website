#By: Adam Mason UMID: adamason 
import webapp2
import os
import logging
import jinja2

#Set up JINJA to know where the template files are stored
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Make One Handler for Home, Food, and Family pages
class OneHandler(webapp2.RequestHandler):
    def get(self):
        #Store path into a variable
        path = self.request.path
        #Set path variable to a string value
        test = str(path)
        #Set template using string concantenation of 'templates' with the path variable 
        template = JINJA_ENVIRONMENT.get_template('templates' + path)
        #Use test variable to represent the path to reference in base template(for capitalization)
        self.response.write(template.render({'path': test}))
        logging.info(path)
        logging.info(test)

#Handler for the Loading or first page/ Special case('/') so hardcoding file name is fine  
class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	#Load index html for first page ('/')
        template = JINJA_ENVIRONMENT.get_template('templates/PortfolioBase.html')
        #Set 'path' to /index.html to reference in base
        self.response.write(template.render({'path': '/index.html'}))

#Handler for Login page 
class FormHandler(webapp2.RequestHandler):
    def get(self):
        #Load login.html
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        #Set 'path' to /login.html to reference in base
        self.response.write(template.render({'path' : '/login.html'}))
    def post(self):
        #Get Username and Password from form
        userName = self.request.get('name')
        passWord = self.request.get('pw')
        #If valid, load Success message(in login2.html) and set 'path' for reference in base
        if userName == 'Colleen' and passWord == "pass":
            template = JINJA_ENVIRONMENT.get_template('templates/login2.html')
            self.response.write(template.render({'path' : '/login.html'}))
        #If invalid, log the bad info. and render the form again
        else:
            logging.info('********BAD USERNAME*********:' + str(userName))
            logging.info('********BAD PASSWORD*********:' + str(passWord))
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            #Set error message and path for base template
            self.response.write(template.render({'Bad' : 'Bad credentials. Try again.', 'path' : '/login.html'}))

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/login.html', FormHandler),
    ('/.*.html', OneHandler)
    
], debug=True)
