import re

file = open('Games.txt', 'r')

gameSum = 0

def getPower(deconstructedGame):
  minCubes = {'red': 0, 'green': 0, 'blue': 0}
  # check every element except 'Game X'
  for coloredCubes in deconstructedGame[1:]:
    # [0]: number of cubes [1]: color of cubes
    splitColoredCubes = re.split(r' ', coloredCubes.strip())
    cubeColor = splitColoredCubes[1]
    cubeNumber = int(splitColoredCubes[0])
    if (minCubes[cubeColor] < cubeNumber):
      minCubes[cubeColor] = cubeNumber
  
  power = 1
  for i in minCubes:
    power = power * minCubes[i]

  return power

    

for line in file:
  deconstructedGame = re.split(':|,|;', line)
  gamePower = getPower(deconstructedGame)
  gameSum += gamePower

print('Total Sum:', gameSum)