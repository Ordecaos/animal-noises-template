from flask import Flask, Response, request
import random

app = Flask(__name__)

# animal generator route here

@app.route("/animal/name", methods=["GET"])
def animal():
    animal_names = ["Pig", "Cow", "Dog"]
    animal_choice = random.choice(animal_names)
    return Response(animal_choice, mimetype="text/plain")

animal_type = animal()


# animal noise generator route here

@app.route("/animal/noise", methods=["POST"])
def noise():
    animal = request.data.decode('utf-8')
    if animal == 'Pig':
        noise = 'Oink'
    elif animal == 'Cow':
        noise = 'Moo'
    elif animal == 'Dog':
        noise = 'Woof'
    else:
        noise = 'There is no noise for that'
    #key = animal_type
    #animal_noises = {"Pig": "oink", "Cow": "moow", "Dog": "woof"}
    #noise_choice = animal_noises[key]
    return Response(noise, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)