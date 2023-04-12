from flask import Flask
from views import views #import the views var from views.py to initialise flask

# initialise flask 
app = Flask(__name__)

#connect to blueprint
#url_prefix to initialise which page it goes to when loaded
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)