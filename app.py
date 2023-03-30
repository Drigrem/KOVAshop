from flask import Flask, url_for, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)