from flask import Flask, render_template, request
import random
import itertools
import smtplib

application = Flask(__name__)
words_grid = []
color_grid = []
starting_color = ""

@application.route('/')
def choice():
    return render_template("choice.html")


@application.route('/start/')
def start():
    global words_grid
    global color_grid
    global starting_color
    words_grid = createWordsGrid()
    color_grid, starting_color = createColorGrid()
    #emailColorGrid(color_grid, starting_color)
    return board()


@application.route('/board/')
def board():
    global words_grid
    global color_grid
    global starting_color
    if not words_grid:
        words_grid = createWordsGrid()
        color_grid, starting_color = createColorGrid()
    return render_template("board.html", words_grid=words_grid, color_grid=color_grid, starting_color=starting_color)


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


def emailColorGrid(color_grid, starting_color):
    emails = ["email1@gmail.com", "email2@gmail.com"]
    message = createMessage(color_grid, starting_color)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("emailid", "password")
    for email in emails:
        s.sendmail("rohan@jaisimha.com", email, message)
    s.quit()

def createMessage(color_grid, starting_color): 
    message = "Subject: Your Codenames key"
    message += "\nContent-Type: text/html; charset='UTF-8'"
    message += "\n\n"
    message += "<html><head><style>td{margin:3px;padding:3px;height:113px;width:113px;text-align:center;font-weight:bold;font-size:150%;}</style></head><body><table><tbody><tr>"
    message += "<td colspan='5' style='background-color:" + starting_color + ";'></td>" 
    message += "</tr><tr><td></td></tr>"
    for row in color_grid:
        message += "<tr>"
        for color in row:
            message += "<td style='background-color:" + color + ";'></td>"
        message += "</tr>"
    message += "<tr><td></td></tr><tr>"
    message += "<td colspan='5' style='background-color:" + starting_color + ";'></td>"
    message += "</tr></tbody></table></body></html>"
    return message
    

if(__name__ == "__main__"):
    application.run(debug=True)
