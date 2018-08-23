from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.giphy.com/media/11c7UUfN4eoHF6/giphy.gif",
    "https://media.giphy.com/media/eDgmbiQcujjsA/giphy.gif",
    "https://media.giphy.com/media/Ov5NiLVXT8JEc/giphy.gif",
    "https://media.giphy.com/media/NqZn5kPN8VVrW/giphy.gif",
    "https://media.giphy.com/media/B6odR0DhsStfW/giphy.gif",
    "https://media.giphy.com/media/B6odR0DhsStfW/giphy.gif",
    "https://media.giphy.com/media/13borq7Zo2kulO/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif",
    "https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif",
    "https://media.giphy.com/media/tBxyh2hbwMiqc/giphy.gif",
    "https://media.giphy.com/media/Hcw7rjsIsHcmk/giphy.gif",
    "https://media.giphy.com/media/GtZzfs0KuEjQY/giphy.gif",
    "https://media.giphy.com/media/L76sH9DjvVyik/giphy.gif",
    "https://media.giphy.com/media/MpSgICvhxS2kw/giphy.gif",
    "https://media.giphy.com/media/hXafx5jj9HVBe/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
