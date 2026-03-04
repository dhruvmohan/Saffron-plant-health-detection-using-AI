from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "root_rot": random.randint(0,100),
        "fungal": random.randint(0,100),
        "nutrient": random.randint(0,100),
        "dehydration": random.randint(0,100),
        "mold": random.randint(0,100)
    }
    return render_template("index.html", data=data)

app.run(debug=True)
