from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/option")
def option():
    return render_template('option.html')
app.run(debug=True)
