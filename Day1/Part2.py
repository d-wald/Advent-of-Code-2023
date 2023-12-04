file = open("CalibrationValues.txt", "r")
calibrationSum = 0
digitList = ["one","two","three","four","five","six","seven","eight","nine"]

def checkIfNumber(startPosition, endPosition, line):
  if(endPosition < len(line)):
    word = line[startPosition:endPosition+1]
    if(word in digitList):
      return digitList.index(word) + 1

  return -1

for line in file:
  numbersInLine = []
 
  for i in range(0,len(line)):
    char = line[i]
    digit = 0
    if char.isdigit():
      numbersInLine.append(char)
    else:
      if char == 'o':
        digit = checkIfNumber(i, i+2, line) #one
      elif char == 't':
        digit = checkIfNumber(i, i+2, line) #two
        if digit < 0:
          digit = checkIfNumber(i, i+4, line) #three
      elif char == 'f':
        digit = checkIfNumber(i, i+3, line) #four or five
      elif char == 's':
        digit = checkIfNumber(i, i+2, line) #six
        if digit < 0:
          digit = checkIfNumber(i, i+4, line) #seven
      elif char == 'e':
        digit = checkIfNumber(i, i+4, line) #eight
      elif char == 'n':
        digit = checkIfNumber(i, i+3, line) #nine
      
      if (digit > 0):
        numbersInLine.append(digit)
  
  calibrationNumber = f'{numbersInLine[0]}{numbersInLine[-1]}'
  calibrationSum += int(calibrationNumber)

print("Total Sum:", calibrationSum)