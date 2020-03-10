# Exercise: omitting notes and just adding the necessary code
from flask import Flask
app = Flask(__name__)
from application import routes
from application import app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')