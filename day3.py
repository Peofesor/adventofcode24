import re
#with open('inputday3.txt', 'r') as file: input = file.read()

input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
#print(input)

pattern = r"don't|do|mul\((\d+),(\d+)\)"

valid_mul_pairs = []

is_allowed = True

matches = re.findall(pattern, input)

for match in matches:
    valid_mul_pairs.append([int(match[0]), int(match[1])]) # error here probably since not every match consists of 2 groups

print(valid_mul_pairs)

result = 0

for pair in valid_mul_pairs:
    result += pair[0] * pair[1]

print(result)

# regexr.com 