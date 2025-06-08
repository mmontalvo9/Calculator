from flask import Flask, render_template, request
import math
import numpy as np
import matplotlib.pyplot as plt
import os
import logging

app = Flask(__name__)
expression = ""
mode = "radians"  # default mode

# Logging setup (ensures visibility in Render)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def calculator():
    global expression, mode
    result = ""

    if request.method == "POST":
        btn = request.form["btn"]
        app.logger.info(f"Button pressed: {btn}")

        if btn == "TOGGLE_MODE":
            mode = "degrees" if mode == "radians" else "radians"
            app.logger.info(f"Mode switched to: {mode}")
        elif btn == "C":
            expression = ""
        elif btn == "DEL":
            expression = expression[:-1]
        elif btn == "=":
            try:
                expr = expression.replace('^', '**').replace('π', str(math.pi)).replace('√', 'math.sqrt').replace('ln', 'math.log')
                if mode == "degrees":
                    expr = expr.replace('sin', 'math.sin(math.radians')
                    expr = expr.replace('cos', 'math.cos(math.radians')
                    expr = expr.replace('tan', 'math.tan(math.radians')
                    expr = expr.replace('asin', 'math.degrees(math.asin')
                    expr = expr.replace('acos', 'math.degrees(math.acos')
                    expr = expr.replace('atan', 'math.degrees(math.atan')
                    expr = expr.replace(')', '))')
                else:
                    expr = expr.replace('sin', 'math.sin')
                    expr = expr.replace('cos', 'math.cos')
                    expr = expr.replace('tan', 'math.tan')
                    expr = expr.replace('asin', 'math.asin')
                    expr = expr.replace('acos', 'math.acos')
                    expr = expr.replace('atan', 'math.atan')
                expr = expr.replace('!', 'math.factorial')
                result = str(eval(expr))
                expression = result
            except Exception as e:
                app.logger.error(f"Evaluation error: {e}")
                result = "Error"
                expression = ""
        else:
            expression += btn
            result = expression

    return render_template("index.html", result=result, mode=mode)

@app.route("/graph", methods=["GET", "POST"])
def graph():
    global mode
    show_graph = False

    if request.method == "POST":
        app.logger.info("Received POST at /graph")

        if "TOGGLE_MODE" in request.form:
            mode = "degrees" if mode == "radians" else "radians"
            app.logger.info(f"Mode toggled to: {mode}")
        else:
            equation = request.form["equation"]
            app.logger.info(f"Equation received: {equation}")

            try:
                expr = equation.replace("^", "**").replace("π", str(math.pi))
                x = np.linspace(-360 if mode == "degrees" else -10, 360 if mode == "degrees" else 10, 400)

                def wrap_func(f):
                    return lambda val: f(np.radians(val)) if mode == "degrees" else f(val)

                allowed_names = {
                    "x": x,
                    "sin": wrap_func(np.sin),
                    "cos": wrap_func(np.cos),
                    "tan": wrap_func(np.tan),
                    "asin": wrap_func(np.arcsin),
                    "acos": wrap_func(np.arccos),
                    "atan": wrap_func(np.arctan),
                    "log": np.log,
                    "sqrt": np.sqrt,
                    "pi": np.pi,
                    "e": np.e,
                    "abs": np.abs
                }

                y = eval(expr, {"__builtins__": {}}, allowed_names)
                app.logger.info("Eval successful")

                plt.figure(figsize=(6, 4))
                plt.plot(x, y)
                plt.grid(True)
                plt.title(f"y = {equation} ({mode})")
                plt.xlabel("x")
                plt.ylabel("y")

                os.makedirs("static", exist_ok=True)
                plt.savefig("static/graph.png")
                plt.close()

                app.logger.info("Graph saved to static/graph.png")
                show_graph = True

            except Exception as e:
                app.logger.error(f"Graphing error: {e}")
                show_graph = False

    return render_template("graph.html", show_graph=show_graph, mode=mode)

# ✅ Compatible with Render.com (binds to external port)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)






