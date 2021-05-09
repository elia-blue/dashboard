from flask import Flask, request, render_template

from .widgets import ClockWidget, PingWidget

app = Flask(__name__)

widgets = [
    ClockWidget(),
    PingWidget(["10.0.0.1"])
]

@app.route("/")
def index_page():
    return render_template("index.html", widgets=widgets)
