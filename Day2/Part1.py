import re

file = open('Games.txt', 'r')

gameSum = 0
possibleWinCondition = {'red': 12, 'green': 13, 'blue': 14}

def possibleGame(deconstructedGame):
  # check every element except 'Game X'
  for coloredCubes in deconstructedGame[1:]:
    # [0]: number of cubes [1]: color of cubes
    splitColoredCubes = re.split(r' ', coloredCubes.strip())
    if (possibleWinCondition[splitColoredCubes[1]] < int(splitColoredCubes[0])):
      return 0
    
  # deconstructedGame[0]: 'Game X'
  # split[0]: 'Game' split[1]: 'X'
  return int(re.split(r' ', deconstructedGame[0])[1])

    

for line in file:
  deconstructedGame = re.split(':|,|;', line)
  game = possibleGame(deconstructedGame)
  gameSum += game

print('Total Sum:', gameSum)