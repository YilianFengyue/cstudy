from flask import Flask
app = Flask(__name__)

@app.route('/')
#Test4
def index():
    return 'Hello World!'
app.run(debug=True)