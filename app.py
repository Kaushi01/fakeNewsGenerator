from flask import Flask, render_template
import os, random

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))



Subjects = [
    "Donald Trump",
    "Narendra Modi",
    "Priyanka Chopra",
    "Salman Khan",
    "Hardik Pandya",
    "Elon Musk",
    "Taylor Swift",
    "Virat Kohli",
    "Bill Gates",
    "Kylie Jenner",
    "Ranveer Singh",
    "Shah Rukh Khan",
    "Cristiano Ronaldo",
    "Kim Kardashian",
    "Drake",
    "Deepika Padukone",
    "Messi",
    "Kangana Ranaut",
    "Robert Downey Jr."
]

Activity = [
    " fell off the bed while winning an argument in my head",
    " chased by a dog for existing",
    " tried yoga, achieved paralysis",
    " is stuck in traffic again",
    " arguing with paparazzi in pajamas",
    " accidentally joined a Zoom class instead of a meeting",
    " fell asleep during their own speech",
    " bought an island on impulse after missing breakfast",
    " declared that Mondays should be illegal",
    " was spotted arguing with a mirror for 2 hours",
    " tried to cook Maggi and set off national alarms",
    " started a band called '404 Not Found'",
    " claims they can time travel using WiFi",
    " released a perfume that smells like success and confusion",
    " just admitted their pet runs their social media account"
]

Location = [
    "Delhi",
    "Mumbai",
    "Jaipur",
    "USA",
    "a secret beach",
    "India Gate",
    "a traffic jam on Mars",
    "a coffee shop for billionaires",
    "a live interview",
    "a mysterious party",
    "Parliament House",
    "New York City",
    "a plane to nowhere"
]


@app.route('/')
def home():
    sub = random.choice(Subjects)
    act = random.choice(Activity)
    loc = random.choice(Location)

    # 🧠 Smart preposition logic
    if loc in ["Delhi", "Mumbai", "Jaipur", "New York City"]:
        preposition = "in"
    elif loc in ["USA", "India"]:
        preposition = "in the"
    else:
        preposition = "at"

    headline = f"{sub}{act} {preposition} {loc}"
    return render_template('index.html', headline=headline)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

