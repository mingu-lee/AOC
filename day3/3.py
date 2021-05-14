def gun(t,r,c,l):
    while r+1 < len(l):
        r +=1
        c +=3

        way = l[r][c % len(l[r])]
        if way == "#":
            t +=1
    return t

if __name__ == "__main__":
    f = open("day3/puzzle.txt", 'r')
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    treeCount =0
    row =0
    col =0

    print(gun(treeCount, row, col, lines))