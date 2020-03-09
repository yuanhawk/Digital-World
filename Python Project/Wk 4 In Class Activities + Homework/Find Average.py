def find_average(inp):
  array = []
  array.extend(inp)

  avg = 0
  counter = 0
  subavgarray = []  #Store in innerarrayavg

  

  for i in range(len(array)):   #i is increment of array
    subavg = 0
    count = 0
    for j in range(len(array[i])):
      avg += array[i][j]
      subavg += array[i][j]
      counter += 1
      count += 1

    if count != 0:  
      subavg /= count
      subavgarray.append(subavg)  #Append value to subavgarray
    else:
      subavg = 0.0
      subavgarray.append(subavg)

  avg /= counter
  
  return subavgarray, avg