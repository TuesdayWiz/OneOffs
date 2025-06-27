from tkinter import Tk, N, E, S, W, Frame, Checkbutton, Label, Scrollbar

"""
TODO:
- Get tkinter set up
- Create buttons that create a Play object
    - Global var that changes every play (tracks turns)
    - Function that creates Play based on the var
- Port literally all of this to work with tkinter
"""

possible_wins = {
    # Use this to streamline win checking
    'rows': [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    'columns': [[0, 3, 6], [1, 4, 7], [2, 5, 8]],
    'diagonals': [[0, 4, 8], [2, 4, 6]]
}

board = [
    '~', '~', '~',
    '~', '~', '~',
    '~', '~', '~'
]
# This needs to be initialized as a 9-long array so moves made can replace existing indices instead of creating them

class Play():
    """An object with the required methods and variables needed to manage a 'play'
    """
    def __init__(self, symbol: str, pos: int) -> None:
        self.symbol = symbol
        self.pos = pos  # This may end up going unused.  If so, remove it.
        board[pos] = self
        self.ttl = 4
    
    def move_made(self):
        """Handles what happens to a given object when a play is made (mostly TTL stuff)
        """
        self.ttl -= 1

        if self.ttl <= 0:
            # The board contains the only reference to a given Play object, so replacing the reference with a tilde ends up deleting it
            board[self.pos] = '~'
    
    def __str__(self) -> str:
        return self.symbol

def d_printboard():
    """DEBUG FUNCTION:\n
    Prints the current state of the board to the console
    """
    for i in range(3):
        print(f'-{str(board[0 + (3 * i)])}-{str(board[1 + (3 * i)])}-{str(board[2 + (3 * i)])}-')

def update_board():
    """Handles TTL logic and win-checking
    """
    # Does this first so moves dissapear before checking wins
    for b in board:
        if type(b) == Play:
            b.move_made()
    
    # Win checking
    for char in ['x', 'y']:
        print(f'-----{char}-----')
        for t in list(possible_wins.keys()):
            print(f'Checking {t}...')
            for w in possible_wins[t]:
                if (str(board[w[0]]) == char) and ((str(board[w[1]])) == char) and ((str(board[w[2]])) == char):
                    print(f'{char} wins with type {t}!')

# Creates the root window
root = Tk()
root.title("Endless Tic-Tac-Toe")

# Sets up the grid for use in positioning
mainframe = Frame(root, borderwidth=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Runs the main window loop
root.mainloop()
