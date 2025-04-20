"""This script reads a text file named 'text2.txt', extracts all the words,
and prints the set of unique words found in the file.

It handles potential IOError exceptions if the file is not found
in the current directory.
"""

testSet = set()

try
    # Open input file: numbers.text
    inputFile = open("text2.txt", 'r')

    for line in inputFile:
        line = line.strip()
        items = line.split()

        for item in items:
            testSet.add(item)c

    inputFile.close()

except IOError:
    print("IOError: the numbers.txt file cannot be found in this directory.")

print("Unique words found in the file: ", testSet)