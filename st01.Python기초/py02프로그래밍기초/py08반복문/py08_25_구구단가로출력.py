for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str = "%2s * %s = %3s" % (i, j, i*j)

        if(j == 9):
            print(str, end=".")
        else:
            print(str, end=",")
    print()
