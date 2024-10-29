#!/usr/bin/python3
import sys

# Allow user to choose which file to manipulate
file = input("Which file? ")

# Allow user to define the number of cuts, ensuring it's an integer
number = int(input("How many cuts needed? "))

# Open the file once
with open(file, 'r') as f:
    f_content = f.read()
    print(len(f_content))

# Initialize final sequence
finalseq = ""

# Get the cut positions and slice the sequence
for i in range(number):
    start = int(input(f"Where to start cut {i + 1}? ")) - 1  # Convert to 0-based index
    stop = int(input(f"Where to stop cut {i + 1}? "))
    finalseq += f_content[start:stop]

# Write the result to an output file
output_path = f"{file}_out"
with open(output_path, "w") as fileout:
    fileout.write(finalseq)

print(f"Final sequence saved to {output_path}")
