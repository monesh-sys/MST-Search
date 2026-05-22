from flask import Flask, render_template, request
import json

app = Flask(__name__)

# LOAD WEBSITES

try:

    with open("data.json", "r") as file:

        websites = json.load(file)

except:

    websites = []


# HOME PAGE

@app.route("/", methods=["GET", "POST"])

def home():

    results = []

    if request.method == "POST":

        search = request.form["search"].lower()

        for site in websites:

            if (
                search in site["title"].lower()
                or
                search in site["description"].lower()
            ):

                results.append(site)

    return render_template(
        "index.html",
        results=results
    )


# ADD WEBSITE PAGE

@app.route("/add", methods=["GET", "POST"])

def add():

    if request.method == "POST":

        title = request.form["title"]

        link = request.form["link"]

        description = request.form["description"]

        new_site = {

            "title": title,

            "link": link,

            "description": description
        }

        websites.append(new_site)

        # SAVE TO JSON

        with open("data.json", "w") as file:

            json.dump(websites, file, indent=4)

        # SUCCESS PAGE

        return render_template("success.html")

    return render_template("add.html")


# RUN WEBSITE

app.run(host="0.0.0.0", port=5000, debug=True)