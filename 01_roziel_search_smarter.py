scores = [1, 3, 5, 7, 9, 11, 13, 15, 17]

input("The list is: " + str(scores) + "press enter to continue: ")
guess = input("Guess how many checks it will take to find numbers inside of the list: ")
target = int(input("Guess a number from the list: "))

input("binary search cuts the numbers in half repeatedly, press enter: ")
low, high = 0, len(scores) - 1

steps = 0
while low <= high:
    mid = (low + high) // 2
    steps += 1
    print("round", steps, "-> checked", scores[mid])
    if scores[mid] == target:
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print("found", target, "at position", mid + 1, "checked", steps, "guess:", guess, "-> 0(log n)")

input("steps grow slowly along with n, press enter:")
for n, s in [(9,4), (100, 7), (1000, 10)]:
    print("n is ", n, "miximum steps is ", s)