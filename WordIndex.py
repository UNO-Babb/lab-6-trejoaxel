#WordIndex.py
#Name: Axel
#Date: 02/26/25
#Assignment: WordIndex

def main():
  textFile = open("fish.txt", 'r')
  
  wordList = {} #create an empty dictionary
  
  lineNum = 0 
  for line in textFile:
    lineNum = lineNum + 1
    words = line.split()
    for word in words:
      word = word.lower()
      word = word.replace("," , "")
      word = word.replace("." , "")
      word = word.replace("!" , "")
      word = word.replace("/n" , "")


      if word in wordList:
        wordList[word].append(lineNum)  #adding to existing entry
      else: 
        wordList[word] = [lineNum]      #add word to list 
      
  print(wordList)
  for word in wordList:
    print(word, wordList[word])


  '''''
  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)
  '''''

if __name__ == '__main__':
  main()
