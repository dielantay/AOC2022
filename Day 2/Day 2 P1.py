f = open("C:\\Users\\Admin\\Desktop\\coding tryout\\Day 2\\day2 AOC dataset.txt", "r")
dataset = f.read().split("\n")

for letter in dataset:
    word = letter.split(" ")
    print(word)
    for j in word:
        if j[0] == "A" and j[1] == "X":
            j == "4"
        if j[0] == "B" and j[1] == "X":
            j == "7"
        if j[0] == "C" and j[1] == "X":
            j == "3"

        if j[0] == "A" and j[1] == "Y":
            j == "4"
        if j[0] == "B" and j[1] == "Y":
            j == "7"
        if j[0] == "C" and j[1] == "Y":
            j == "3"
        