class Queen:

    # initializing the values for object of the queen class
    def __init__(self, n=N):
        self.n = n
        self.found = 0
        # to know the position of the queen in the column
        self.board = [None] * n
        # to check if the row is safe
        self.row = [0] * n
        # to check if the downward diagonal is safe
        self.down = [0] * (2 * n + 1)
        # to check if the upward diagonal is safe
        self.up = [0] * (2 * n - 1)
        self.solveNQ()

    # recursive check to find the position
    def solveNQ(self, x=0):
        for y in range(self.n):
            if self.isSafe(x, y):
                self.board[x] = y
                self.row[y] = self.down[x + y] = self.up[x - y] = 1
                if x + 1 == self.n:
                    self.printNQ()
                else:
                    self.solveNQ(x + 1)
                self.board[x] = None
                self.row[y] = self.up[x - y] = self.down[x + y] = 0

    # to check if the position found is safe to place the queen
    def isSafe(self, x, y):
        if (not self.row[y] and not self.down[x + y] and not self.up[x - y]):
            return True
        else:
            return False

    # to print the output in the required format
    def printNQ(self):
        self.found = self.found + 1
        if (self.found < 5):
            print()
            for x in range(self.n):
                for y in range(self.n - 1):
                    if self.board[x] == y:
                        print("(", x, ",", y, end=')')


def main():
    n = N
    Queen(n)


def print_result():
    main()