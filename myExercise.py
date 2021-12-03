import sys
with open("students.txt") as f:
    notes = dict()
    for line in f:
        if "\n" in line:
            line = line[:-1]
            line = line.split(":")
            notes[line[0]] = line[1]
        else:
            line = line.split(":")
            notes[line[0]] = line[1]
    students = sys.argv[2].split(",")
    for i in students:
        try:
            print(i,notes[i],end="")
        except KeyError:
            print("No record of ‘Ahmet’ was found!",end="")
        