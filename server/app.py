from flask import Flask, request, Response, render_template
import requests

app = Flask(__name__)

# home route here

@app.route('/')
def home():
    return render_template('layout.html')

# must query the animal API for an animal and a noise – the noise should be based on the animal

@app.route('/index', methods=['GET'])
def noises():
    animal = requests.get('http://animal_api:5000/')
    noise = requests.get('http://animal_api:5000/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)