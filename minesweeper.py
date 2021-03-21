import random
    #make a grid, with variables with interchangeable size
    #place the mines
    #ask for input
def build_grid(n):
    y = 0
    x = 0
    value = 0
    for x in range(n):
        print(n*("| " + str(value) + "  "))
        print(n*"|____")
    arr = [[0 for row in range(n)] for column in range(n)]
    print(arr)
    for lst in arr:
        print(lst)
    #place the mines randomly in a list of lists
    number_of_mines = int(input("Enter number of mines: "))
    for num in range(number_of_mines):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        used_cells = []
        if [x, y] in used_cells:
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
        used_cells.append([x, y])
        arr[y][x] = 'X'
        #check right
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center

    for row in arr:
        print("\t".join(str(cell) for cell in row))
        print("")

    for lst in arr:
        print(lst)
    return





new_sweeper = build_grid(8)