from funcs import *

def main():
   string = getInput()
   userInput = userWord()
   print()
   print()
   printPuzzle(string)
   print()
   print()
   words = userInput.split()
   for word in words:
      if checkForward(string, word) is not None:
         print(checkForward(string, word))
      elif checkBackward(string, word) is not None:
         print(checkBackward(string, word))
      elif checkDown(string, word) is not None:
         print(checkDown(string, word))
      elif checkUp(string, word) is not None:
         print(checkUp(string, word))
      elif checkDiagonal(string, word) is not None:
         print(checkDiagonal(string, word))
      else:
         print(word, ": word not found")
   



if __name__ == '__main__':
   main()