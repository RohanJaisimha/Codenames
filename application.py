from flask import Flask, render_template, request
import random
import itertools
import smtplib

application = Flask(__name__)
words_grid = []
color_grid = []
starting_color = ""

@application.route('/')
def index():
    return render_template("index.html")


@application.route('/start/')
def start():
    global words_grid
    global color_grid
    global starting_color
    words_grid = createWordsGrid()
    color_grid, starting_color = createColorGrid()
    return board()


@application.route('/board/')
def board():
    global words_grid
    global color_grid
    global starting_color
    if not words_grid:
        words_grid = createWordsGrid()
        color_grid, starting_color = createColorGrid()
    color_grid_code = encodeColorGrid(color_grid)
    return render_template("board.html", words_grid=words_grid, color_grid=color_grid, starting_color=starting_color, color_grid_code=color_grid_code)


@application.route('/key/')
def key():
    return render_template("key.html")


def createWordsGrid():
    fin = open("words.txt", 'r')
    words = [line.strip() for line in fin.readlines()]
    fin.close()
    words = random.sample(words, 25)
    words_grid = [words[0:5], words[5:10],
                  words[10:15], words[15:20], words[20:25]]
    return words_grid


def createColorGrid():
    grid = [[None]*5 for i in range(5)]
    starting_color = "Red" if random.randrange(0, 2) == 1 else "Blue"
    indices = [*itertools.product(range(5), range(5))]
    random.shuffle(indices)
    for i in range(25):
        row_idx = indices[i][0]
        col_idx = indices[i][1]
        if(0 <= i < 9):
            grid[row_idx][col_idx] = starting_color
        elif(9 <= i < 17):
            grid[row_idx][col_idx] = "Blue" if starting_color == "Red" else "Red"
        elif(i == 17):
            grid[row_idx][col_idx] = "Black"
        else:
            grid[row_idx][col_idx] = "#FFFDD0" #Cream
    return grid, starting_color


def encodeColorGrid(color_grid):
    color_codes = {"Black": '0', "Blue": '1', "#FFFDD0": '2', "Red": '3'}
    code = ""
    for row in color_grid:
        for color in row:
            code += color_codes[color]
    return int(code, 4)
    

if(__name__ == "__main__"):
    application.run(host="0.0.0.0", port=5000, debug=True)
