#WordCount.py
#Name: Axel
#Date: 02/26/25
#Assignment: WordCount

def main():
  textFile = open("fish.txt", 'r')
  
  lineCount = 0
  wordCount = 0
  letterCount = 0 

  for line in textFile:
    lineCount += 1
    words = line.split()

    for word in words:
      wordCount += 1
      print(word)

      for letter in word:
        letterCount += 1
        print(letter)
  
  print("Lines", lineCount, wordCount, letterCount)

if __name__ == '__main__':
  main()
