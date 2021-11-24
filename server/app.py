from flask import Flask, request, Response, render_template
import requests

app = Flask(__name__)

# home route here

@app.route('/', methods=['GET'])
def animals():
    animal = requests.get('http://animal_api:5000/animal/name')
    noise = requests.post('http://animal_api:5000/animal/noise', data=animal.text)
    return render_template('index.html', animal=animal,text, noise=noise,text)

# must query the animal API for an animal and a noise – the noise should be based on the animal

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)