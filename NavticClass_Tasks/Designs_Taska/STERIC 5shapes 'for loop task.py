def draw_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print("^", end="")
        print()

def draw_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

def draw_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def draw_arrow(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def draw_pentagon(size):
    for i in range(size):
        print(" " * (size - i) + "$" * (2 * i + 1))
    for i in range(size // 2):
        print(" " * (size - (size // 2) + i) + "*" * (size + size - 1))

# Call the functions with specific sizes to draw the shapes
draw_rectangle(5, 3)
print()
draw_triangle(5)
print()
draw_square(4)
print()
draw_arrow(5)
print()
draw_pentagon(5)
