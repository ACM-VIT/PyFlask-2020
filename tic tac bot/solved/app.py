from flask import Flask, render_template, request
from utils.minimax import bestMove
from utils.calcscore import check

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def home():
    grid = [""]*9
    return render_template('index.html',grid=grid)

@app.route('/play')
def play():
    g = request.args['grid']
    grid = g.split(',')

    if grid.count('') == 0:
        res = check(grid)
        if res!='D':
            res = res+" Wins!"
        else:
            res = "Its a Draw"
        return render_template('result.html',grid=grid,res=res)

    move = bestMove(grid)
    grid[move] = 'O'
    res = check(grid)
    if res!='D':
        res = res+" Wins!"
        return render_template('result.html',grid=grid,res=res)
    else:
        return render_template('index.html',grid=grid)
if __name__ == '__main__':
    app.run()