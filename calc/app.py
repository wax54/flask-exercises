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
    
@app.route("/sub")
def sub_a_and_b():
    """handles subtraction functionality"""
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.sub(a,b))
    except Exception as e:
        return f"{e}"
    
@app.route("/mult")
def mult_a_and_b():
    """handles multiply functionality"""
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.mult(a,b))
    except Exception as e:
        return f"{e}"
    
@app.route("/div")
def div_a_and_b():
    """handles division functionality"""
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(operations.div(a,b))
    except Exception as e:
        return f"{e}"
    
math = {
    'add': operations.add,    
    'sub': operations.sub,
    'mult': operations.mult,    
    'div': operations.div
}

@app.route("/math/<operation>")
def operate_on_a_and_b(operation):
    """handles add,sub,div, mult functionality"""
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        return str(math.get(operation, f"invalid operation {operation}")(a,b))
    except Exception as e:
        return f"{e}"