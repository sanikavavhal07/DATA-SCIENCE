def right_angled_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

right_angled_triangle(5)
