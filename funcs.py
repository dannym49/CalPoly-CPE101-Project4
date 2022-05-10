# Put your functions in here.
# Feel free to run your design past me before beginning to implement.

def getInput():
    string = input("")
    print()
    return string  

def userWord():
    user = input("")
    return user

def printPuzzle(puzzle):
    print("Puzzle:")
    print()
    for count in range(len(puzzle)):
        if count % 10 != 0 or count == 0:
            print(puzzle[count], end="")
        else:
            print()
            print(puzzle[count], end="")

def flipString(userInput):
    reverse = userInput[::-1]
    return reverse

def checkForward(userInput, words):
    puzzle = []
    res = ""  
    for i in range(10):
        puzzle.append(userInput[10 * i:(10 * i) + 10])  #creates a list and each index is one row of the puzzle
    for row in range(len(puzzle)): 
        if (puzzle[row].find(words)) > -1:
            col = puzzle[row].find(words)  
            res = "%s: %s row: %s column: %s" % (words, '(FORWARD)', row, col)
            return res
    return None

def checkBackward(inputString, word):
    reverse = flipString(word)  
    puzzle = []
    res = ""
    for i in range(10):  
        puzzle.append(inputString[10 * i:(10 * i) + 10])
    for row in range(len(puzzle)):  
        if (puzzle[row].find(reverse)) > -1:
            col = puzzle[row].find(reverse)  
            res = "%s: %s row: %s column: %s" % (word, '(BACKWARD)', row, col + len(reverse) - 1)
            return res
    return None

def checkDiagonal(userInput, words):
    res = ""
    j = 10
    main = []# this section checks the upper diagnols
    puzzle = []
    index = j = 0
    r = 10
    while j < 10:
        for i in range(r):
            puzzle.append(userInput[index])
            index += 11
        puzzle = ''.join(puzzle)
        main.append(puzzle)
        j += 1
        index = j
        r -= 1
        puzzle = []
    for i in range(len(main)): 
            if (main[i].find(words)) > -1:
                row = main[i].find(words)
                res = "%s: %s row: %s column: %s" % (words, '(DIAGONAL)', row, col)
                return res
    puzzle2 = [] #this section checks the bottom diagnols
    index = 10
    j = 9
    x = 0
    main2 = []
    while x < 9:
        for i in range(j):
            puzzle2.append(userInput[index])
            index+=11
        puzzle2 = ''.join(puzzle2)
        main2.append(puzzle2)
        puzzle2 = []
        j -= 1
        index = 0
        index = (x+2)*10
        x += 1
    for row in range(len(main2)): 
            if (main2[row].find(words)) > -1:
                col = main2[row].find(words)
                row = col + row + 1
                res = "%s: %s row: %s column: %s" % (words, '(DIAGONAL)', row, col)
                return res
    return None

def transpose_string(string, rowLength):  
    char = len(string)
    start = 0
    newString = ""
    for row in range(start, rowLength):
        for col in range(row, 100, rowLength): 
            newString += string[col] 
    return newString

def checkDown(inputString, word):
    tran = transpose_string(inputString, 10)  
    puzzle = []
    res = ""
    for i in range(10):
        puzzle.append(tran[10 * i:(10 * i) + 10]) 
    for col in range(len(puzzle)): 
        if (puzzle[col].find(word)) > -1:  
            row = puzzle[col].find(word)
            res = "%s: %s row: %s column: %s" % (word, '(DOWN)', row, col)
            return res
    return None

def checkUp(inputString, word):
    tran= transpose_string(inputString, 10) 
    flip = flipString(tran)
    puzzle = []
    res = ""
    for i in range(10):
        puzzle.append(flip[10 * i:(10 * i) + 10])
    for col in range(len(puzzle)):
        if puzzle[col].find(word) > -1:  
            row = 9 - puzzle[col].find(word)
            res = "%s: %s row: %s column: %s" % (word, '(UP)', row, 9 - col)
            return res
    return None