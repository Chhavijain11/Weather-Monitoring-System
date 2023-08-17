#!/usr/bin/env python3

from flask import Flask, render_template
from process import processH, processT
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/apih', methods=['POST'])
def apih():
    output_h = processH()
    return render_template('index.html', output_w=output_h)
@app.route('/apit', methods=['POST'])
def apit():
    output_t = processT()
    return render_template('index.html', output_w=output_t)
if __name__ == "__main__":
    app.run(debug=True)