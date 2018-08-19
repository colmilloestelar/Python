list1 = []
with open('example1.txt') as file1:
    line = file1.readline()
    while line:
        list1.append(int(line))
        line = file1.readline()

list2 = []
with open('example2.txt') as file2:
    line = file2.readline()
    while line:
        list2.append(int(line))
        line = file2.readline()

overlaplist = []
for elem in list1:
    if elem in list2:
        overlaplist.append(elem)

print(overlaplist)