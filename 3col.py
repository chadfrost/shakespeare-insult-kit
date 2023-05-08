#!python3

# Open the file with the list of words
with open('shakespeare.txt', 'r') as f:
    # Read the lines of the file and split them into a list of words
    words = f.read().split()

# Group the words into three columns
col1 = words[::3]
col2 = words[1::3]
col3 = words[2::3]

# Print the three columns
print("col1 =", col1)
print("col2 =", col2)
print("col3 =", col3)
