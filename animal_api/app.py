from flask import Flask

app = Flask(__name__)

# animal generator route here

animals = ["Pig", "Cow", "Dog"]

# animal noise generator route here

noises = ["Oink", "Moo", "Woof"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)