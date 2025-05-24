# Make 90* triangle

def lines():
    line = int(input("Enter a number of lines: "))
    for i in range(1, line+1):
        for j in range(i):
            print("*", end=" ")
        print()

    return f"\nThe {line} of the triangle has been created"

triangle = lines()
print(triangle)
