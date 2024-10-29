final = ""
with open("input.txt") as f:
    for line in f:
        trimmed_line = line[14:].rstrip()  # Remove the first 14 characters and any trailing whitespace
        final += trimmed_line
        print("The length of adapter-free sequence is:", len(trimmed_line))


with open("trimmedDNA.txt","w") as file:
    file.write(final)