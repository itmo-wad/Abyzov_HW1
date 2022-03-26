from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile')
def profile():
    return redirect('/')

app.run(host='localhost', port=5000, debug=True)