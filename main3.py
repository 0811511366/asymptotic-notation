def onSquareTime(n):
    iteration=0
    for i in range (0,n):
        for j in range (0,n):
            print("#", end=" ")
            iteration+=1
        print("")
    print("\n when n is: ", n,"iteration is: ", iteration)
onSquareTime(4)
onSquareTime(5)
onSquareTime(6)