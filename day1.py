import numpy as np

with open('inputday1.txt', 'r') as file: data = [line.strip().split() for line in file]

array = np.array(data, dtype=int)

sorted_left = array[array[:,0].argsort()]
sorted_right = array[array[:,1].argsort()]

array_left = sorted_left[:,0]
array_right = sorted_right[:, 1]

#print(array_left)
#print(array_right)

differences = np.abs(array_left - array_right)
#print(differences)

total_difference = np.sum(differences)

print("Total difference: ", total_difference)