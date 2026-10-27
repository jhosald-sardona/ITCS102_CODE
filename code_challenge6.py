size = int(input("Enter size"))
andoy = 1
for x in range (size):
    for y in range (x):
        print(andoy, end=" ")
        andoy += 1
    print()
