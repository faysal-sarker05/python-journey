for i in range(3):
    for j in range(2):
        print(i, j)



for i in range(2):
    print("Outer:", i)

    for j in range(3):
        print("   Inner:", j)

print("Done")