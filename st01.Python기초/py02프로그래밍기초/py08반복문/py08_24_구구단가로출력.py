for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str = "%2s * %s = %3s" % (i, j, i*j)
        print(str, end=" ")
    print()
