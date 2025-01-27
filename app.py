from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return 'text'

if __name__=="_main":
    app.run()