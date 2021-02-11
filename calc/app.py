# Put your app in here.
from flask import Flask, request
import operations
app = Flask(__name__)

@app.route("/add")
def add_a_and_b():
    """handles add functionality"""
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.add(a,b))
    except Exception as e:
        return f"{e}"