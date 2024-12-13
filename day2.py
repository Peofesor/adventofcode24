def is_safe_array(array):
    print(array)

    is_increasing = True
    is_decreasing = True
    valid_difference = True

    for i, value in enumerate(array[:-1]):
        if value >= array[i+1]:
            is_increasing = False
        
        if value <= array[i+1]:
            is_decreasing = False
        
        if not (1 <= abs(array[i] - array[i+1]) <= 3):
            valid_difference = False

    if (is_increasing or is_decreasing) and valid_difference:
        return True
        
    else:
        return False
    
    
    
with open('inputday2.txt', 'r') as file: data = [list(map(int, line.strip().split())) for line in file]
#array = [1, 3, 6, 7, 9]

count = 0

for array in data:
    if is_safe_array(array):
        count += 1
        print("safe")
    else:
        for i, _ in enumerate(array):
            new_array = array[:i] + array[i+1:]
            if is_safe_array(new_array):
                count += 1
                print("safe with one removal")
                break

print("Amound of safe reports: ", count)