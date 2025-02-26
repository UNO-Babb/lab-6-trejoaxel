#DiceRoll.py
#Name: Axel 
#Date: 02/26/25
#Assignment: DiceRoll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numRolls = 1000000

  for count in range(numRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    rolls[total -2] = rolls[total -2] + 1


    #print(dice1, dice2, total)
  #find the sum total of the two dice
  

  #print statictics for dice rolls
  num = 2
  for r in rolls: 
    precent = round(r / numRolls * 100, 1)
    print(num , ":", r, precent)
    num = num + 1

if __name__ == '__main__':
  main()
