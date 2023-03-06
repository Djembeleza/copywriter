import os
import openai
from flask import Flask, render_template, request, redirect, url_for


openai.api_key = os.getenv("OPEN_AI")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/create", methods=["POST"])
def create():
    full_name = request.form["full_name"]
    position = request.form["position"]
    content = request.form["experience"]

    basePrompt = """Write me a compelling cover letter I can use to apply for a job using the details below. Please make sure that the tone is professional.
    My Full Name: {0}
    Position I am applying for: {1}
    My experience: {2}
    """.format(
        full_name, position, content
    )
    cover_letter = openai.Completion.create(
        model="text-davinci-003", prompt=basePrompt, max_tokens=250, temperature=0.7
    )

    cover_letter = cover_letter.choices[0].text
    cover_letter = cover_letter.replace("\n", "<br>")

    return render_template("home.html", cover_letter=cover_letter)


if __name__ == "__main__":
    app.run(host="192.168.0.199", port="8000", debug=True)
