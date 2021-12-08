'''
1.Flask Request Object:

In the client-server architecture, the request object contains all the data
that is sent from the client to the server. As we have already discussed in the
tutorial, we can retrieve the data at the server side using the HTTP methods.

1	Form:

It is the dictionary object which contains the key-value pair of form
parameters and their values.

2	args:

It is parsed from the URL. It is the part of the URL which is specified
in the URL after question mark (?).

3	Cookies	:
It is the dictionary object containing cookie names and the values.
It is saved at the client-side to track the user session.

4	files:
It contains the data related to the uploaded file.

5	method	:
It is the current request method (get or post).

2.Form data retrieval on the template:

In the following example, the / URL renders a web page customer.html that
contains a form which is used to take the customer details as the input from the customer.

The data filled in this form is posted to the /success URL which triggers the
print_data() function. The print_data() function collects all the data
from the request object and renders the result_data.html file which shows
all the data on the web page.

The application contains three files, i.e., script.py, customer.html, and
result_data.html.

To run this application, we must first run the script.py file using
the command python script.py. This will start the development server on
localhost:5000 which can be accessed on the browser.

Now, hit the submit button. It will transfer to the /success
URL and shows the data entered at the client.

'''
from flask import *

app = Flask(__name__)


@app.route('/')
def customer():
    return render_template('customer.html')


@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("result_data.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)

