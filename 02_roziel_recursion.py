n = int(input("Enter a small number 3 to 5."))
guess = int(input("How many times do you think the funcion will be called when n = " + str(n)))

input("Recursive will call its own function inside of the function. Press enter to run.")
def countdown(num):
    print("call - n =", num)
    if num > 0:
        countdown(num - 1)
countdown(n)

print("Total calls: ", n + 1, "your guess: ", guess, "countdown -> o(n)")

input("Watch size grow linearly with n. Press enter to run.")
for size in [5, 10, 100]:
    print("n is: ", size, "calls: ", size + 1)