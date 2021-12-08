'''
#Delimiters:

Jinga 2 template engine provides some delimiters which can be used in the HTML
to make it capable of dynamic data representation. The template system provides
some HTML syntax which are placeholders for variables and expressions that are
replaced by their actual values when the template is rendered.

The jinga2 template engine provides the following delimiters to escape from the HTML.

{% ... %} for statements
{{ ... }} for expressions to print to the template output
{# ... #} for the comments that are not included in the template output
# ... ## for line statements


from flask import *

app = Flask(__name__)


@app.route('/user/<uname>')
def message(uname):
    return render_template('data.html', name=uname)


if __name__ == '__main__':
    app.run(debug=True)

#Embedding Python statements in HTML:

Due to the fact that HTML is a mark-up language and purely used for the designing
purpose, sometimes, in the web applications, we may need to execute the
statements for the general-purpose computations. For this purpose,
Flask facilitates us the delimiter {%...%} which can be used to embed
the simple python statements into the HTML.

from flask import *

app = Flask(__name__)


@app.route('/table/<int:num>')
def table(num):
    return render_template('print-table.html', n=num)


if __name__ == '__main__':
    app.run(debug=True)


#Referring Static files in HTML:

The static files such as CSS or JavaScript file enhance the display of an HTML
web page. A web server is configured to serve such files from the static folder
in the package or the next to the module. The static files are available
at the path /static of the application.

#Example:

In the following example, the flask script returns the HTML file, i.e., message.
html which is styled using the stylesheet style.css. The flask template system
finds the static CSS file under static/css directory. Hence the style.css is
saved at the specified path.

'''

from flask import *

app = Flask(__name__)


@app.route('/')
def message():
    return render_template('msg.html')


if __name__ == '__main__':
    app.run(debug=True)