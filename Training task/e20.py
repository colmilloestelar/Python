def findN(orl, goal):
    for element in orl:
        if element == goal:
            return True
    return False



l = [2, 4, 6, 8, 10]

print(findN(l, 5))  # prints False
print(findN(l, 6))  # prints True