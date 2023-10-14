ages = [10, 20, 30]

def calculateAverage(list):
  sum = 0
  for i in list:
    sum = sum + i;
  print(sum/len(list))

calculateAverage(ages)