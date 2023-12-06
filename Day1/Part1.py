file = open('CalibrationValues.txt', 'r')

calibrationSum = 0

for line in file:
  numbersInLine = [int(i) for i in line if i.isdigit()]
  calibrationNumber = f'{numbersInLine[0]}{numbersInLine[-1]}'
  calibrationSum += int(calibrationNumber)

print('Total Sum:', calibrationSum)