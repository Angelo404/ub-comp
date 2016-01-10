from Context import Context
from flask import Flask

app = Flask(__name__)
context = Context()

@app.route("/API/update/<key>/<value>")
def update(key, value):
    context.update(key, value)
    return "OK"


app.run()

