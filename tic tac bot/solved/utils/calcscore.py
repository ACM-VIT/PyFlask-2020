def check(grid):
    i = 0
    while i<=6:
        if grid[i] == grid[i+1] and grid[i+1] == grid[i+2]:
            if grid[i] == 'X':
                return 'X'

            if grid[i] == 'O':
                return 'O'

        i+=3

    for i in range(3):
        if(grid[i] == grid[i+3] and grid[i+3] == grid[i+6]):
            if grid[i] == 'X':
                return 'X'
            if grid[i] == 'O':
                return 'O'

    if grid[0] == grid[4] and grid[4] == grid[8]:
        if grid[0] == 'X':
            return 'X'
        if grid[0] == 'O':
            return 'O'

    if grid[2] == grid[4] and grid[4] == grid[6]:
        if grid[2] == 'X':
            return 'X'
        if grid[2] == 'O':
            return 'O'

    return 'D'

def score(grid):
    value = 0
    if check(grid) == 'X':
        value = -10
    elif check(grid) == 'O':
        value = 10

    return value
