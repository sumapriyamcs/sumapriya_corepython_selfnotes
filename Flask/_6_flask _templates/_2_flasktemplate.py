'''
#Flask Templates:

In the previous examples, we have returned the simple string as the response
from the view function. Although, flask facilitates us to return the response
in the form of HTML templates. In this section of the tutorial,
we will go through the ways using which we can return the HTML response from
the web applications.


#Example:

The following flask script contains a view function, i.e., the message()
which is associated with the URL '/'. Instead of returning a simple plain string as a message,
it returns a message with <h1> tag attached to it using HTML.



from flask import *
app = Flask(__name__)
@app.route('/')
def message():
      return "<html><body><h1>Hi, welcome to the website</h1></body></html>"
if __name__ == '__main__':
   app.run(debug = True)
'''

'''
#Rendering external HTML files:
    
Flask facilitates us to render the external HTML file instead of hardcoding 
the HTML in the view function. 
Here, we can take advantage of the jinja2 template engine on 
which the flask is based.

Flask provides us the render_template() function which can be used to render 
the external HTML file to be returned as the response from the view function.

from flask import *

app = Flask(__name__)


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)

'''