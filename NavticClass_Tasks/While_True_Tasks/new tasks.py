


# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
#######You use continue to skip the current iteration, and continue with the next iteration
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

#example
    n = 0

    while n != 3:
        print(n)
        n += 1
    else:
        print(n, "else")

    print()

    for i in range(0, 3):
        print(i)
    else:
        print(i, "else")

    #Example
    #code:

    for i in range(3):
        print(i, end=" ")  # Outputs: 0 1 2

    for i in range(6, 1, -2):
        print(i, end=" ")  # Outputs: 6, 4, 2

