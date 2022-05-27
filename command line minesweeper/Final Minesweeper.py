import random
class Sweeper_Board:
    def __init__(self, dim_size, num_mines):
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = self.make_map_plant_mines()
        self.assign_values_to_board()
        self.swept = set()

    def make_map_plant_mines(self):
        board = [[0 for row in range(self.dim_size)] for column in range(self.dim_size)]
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == 'X':
                continue
            board[row][col] = 'X'
            mines_planted += 1
        return board

    def assign_values_to_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == 'X':
                    continue
                self.board[row][col] = self.num_neighboring_mines(row, col)
        return self.board

    def num_neighboring_mines(self, r, c):
        num_neighbor_mines = 0
        if r < self.dim_size-1 and self.board[r+1][c] == 'X':
            num_neighbor_mines += 1
        if r < self.dim_size-1 and c < self.dim_size-1 and self.board[r+1][c+1] == 'X':
            num_neighbor_mines += 1
        if c < self.dim_size-1 and self.board[r][c+1] == 'X':
            num_neighbor_mines += 1
        if r > 0 and c <self.dim_size-1 and self.board[r-1][c+1] == 'X':
            num_neighbor_mines += 1
        if r > 0 and self.board[r-1][c] == 'X':
            num_neighbor_mines += 1
        if r > 0 and c > 0 and self.board[r-1][c-1] == 'X':
            num_neighbor_mines += 1
        if c > 0 and self.board[r][c-1] == 'X':
            num_neighbor_mines += 1
        if r < self.dim_size-1 and c > 0 and self.board[r+1][c-1] == 'X':
            num_neighbor_mines += 1
        return num_neighbor_mines
            

    def sweep(self, row, col):
        self.swept.add((row, col))
        if self.board[row][col] == 'X':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.swept:
                    continue
                self.sweep(r, c)
        return True

    def __str__(self):
        player_board = [['8==D' for cell in range(self.dim_size)] for cell in range(self.dim_size)]
        big_string = ""
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.swept:
                    player_board[r][c] = str(self.board[r][c])
                else:
                    player_board[r][c] == '$'
        for row in player_board:
            big_string += str("\t".join(str(cell) for cell in row))
            big_string += "\n"
        return big_string

def play():
    user_dim_size = int(input("Be best, and pick a grid size: "))
    user_mines = int(input("Shut up and pick a number of mines: "))
    major_sweepage = Sweeper_Board(user_dim_size, user_mines)    
    #create map
    #place bombs
    #dig recursively
    #repeat until you hit a bomb or spot next to a bomb
    while len(major_sweepage.swept) < user_dim_size**2 - user_mines:
        print(major_sweepage)
        row = int(input("Pick a damn row: "))
        col = int(input("Pick a damn column: "))
        if row < 0 or row > user_dim_size or col < 0 or col > user_dim_size:
            print("try again, guy.")
            continue
        gravy = major_sweepage.sweep(row, col)
        if not gravy:
            break
    if gravy:
        print("FINALLY.")
        print(major_sweepage)
    else:
        print("Terrible job.")
        print(major_sweepage)
play()