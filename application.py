from flask import Flask, render_template, request
import random
import itertools
import smtplib

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/start")
def start():
    words_grid = createWordsGrid()
    color_grid, starting_color = createColorGrid()
    color_grid_code = encodeColorGrid(color_grid)
    return render_template(
        "board.html",
        words_grid=words_grid,
        color_grid=color_grid,
        starting_color=starting_color,
        color_grid_code=color_grid_code,
    )


@application.route("/key")
def key():
    id_string = request.args.get("id")
    return (
        render_template("key_table.html", id=id_string)
        if id_string
        else render_template("key_form.html")
    )


@application.route("/instructions")
def instructions():
    return render_template("instructions.html")


def createWordsGrid():
    fin = open("words.txt", "r")
    words = [line.strip() for line in fin.readlines()]
    fin.close()
    words = random.sample(words, 25)
    words_grid = [words[0:5], words[5:10], words[10:15], words[15:20], words[20:25]]
    return words_grid


def createColorGrid():
    grid = [[None] * 5 for i in range(5)]
    starting_color = "Red" if random.randrange(0, 2) == 1 else "Blue"
    indices = [*itertools.product(range(5), range(5))]
    random.shuffle(indices)
    for i in range(25):
        row_idx = indices[i][0]
        col_idx = indices[i][1]
        if 0 <= i < 9:
            grid[row_idx][col_idx] = starting_color
        elif 9 <= i < 17:
            grid[row_idx][col_idx] = "Blue" if starting_color == "Red" else "Red"
        elif i == 17:
            grid[row_idx][col_idx] = "Black"
        else:
            grid[row_idx][col_idx] = "#FFFDD0"  # Cream
    return grid, starting_color


def encodeColorGrid(color_grid):
    color_codes = {"Black": "0", "Blue": "1", "#FFFDD0": "2", "Red": "3"}
    code = ""
    for row in color_grid:
        for color in row:
            code += color_codes[color]
    return base36encode(int(code, 4))


def base36encode(number, alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    base36 = ""
    sign = ""
    if number < 0:
        sign = "-"
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
    return sign + base36


def base36decode(number):
    return int(number, 36)


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
