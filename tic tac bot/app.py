from flask import Flask, render_template, request
from utils.minimax import bestMove
from utils.calcscore import check

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def home():
    # Home Page
    grid = [""]*9
    return render_template('index.html',grid=grid)

@app.route('/play')
def play():
    # Extract Grid Values
    # Check if Grid is Complete
    # Check for Best Next Move
    return render_template('index.html',grid=grid)

if __name__ == '__main__':
    app.run()
