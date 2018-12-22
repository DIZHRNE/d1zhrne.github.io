from flask import Flask
from datetime import datetime
from datetime import datetime as dt
import time
import webbrowser
app = Flask(__name__)

@app.route('/')
def homepage():



    <h1>Hello heroku</h1>
    <p>The music will play at 12/22/2018 at 2:34.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

