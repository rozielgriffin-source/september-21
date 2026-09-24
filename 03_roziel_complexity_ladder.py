guess = input("What will n be if O(n^2) and n = 1000?")

input("watch the difference between O(n) and O(n^2). Press enter to run.")
for n in [10, 100, 1000]:
    input("n =" + str(n) + "Press enter to run.")
    print("O(n) =", n, "O(n^2) =", n * n)
print("your guess: ", guess)
input("full ladder is n = 1000. Press enter to run.")
print("0(1) = 1 step, 0(log n) = 10 steps, 0(n) = 1000 steps, O(n^2) = 1,000,000 steps.")