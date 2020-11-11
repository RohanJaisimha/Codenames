from bs4 import BeautifulSoup
import requests


def getWords(url):
    data = BeautifulSoup(requests.get(url).text, "html.parser")
    tds = data.find_all("td")
    words = []
    for i in range(9, len(tds), 5):
        word = tds[i].text.strip()
        if 4 <= len(word) <= 10:
            words.append(word)
    return words


def writeToFile(data, filename):
    fout = open(filename, "w")
    for i in data:
        fout.write(i + "\n")
    fout.close()


def main():
    words = getWords("https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx")
    writeToFile(words, "words.txt")


if __name__ == "__main__":
    main()
