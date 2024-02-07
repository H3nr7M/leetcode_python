# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

class GameOfLife:
    def __init__(self, live_cells, steps):
        self.live_cells = live_cells
        self.steps = steps
        self.board = {}
        for cell in live_cells:
            self.board[cell] = True

    def run(self):
        for step in range(self.steps):
            print("Step {}:".format(step))
            self.print_board()
            new_board = {}
            for cell in self.board:
                live_neighbours = self.count_live_neighbours(cell)
                if self.board[cell] and live_neighbours in [2, 3]:
                    new_board[cell] = True
                if not self.board[cell] and live_neighbours == 3:
                    new_board[cell] = True
            self.board = new_board

    def count_live_neighbours(self, cell):
        count = 0
        x, y = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (x + i, y + j) in self.board:
                    count += 1
        return count

    def print_board(self):
        min_x = min(x for x, y in self.board)
        max_x = max(x for x, y in self.board)
        min_y = min(y for x, y in self.board)
        max_y = max(y for x, y in self.board)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in self.board:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()

# Example usage:
live_cells = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)]
game = GameOfLife(live_cells, 5)
game.run()
