'''EPR 07 Aufgabe 3'''
__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

from os import get_terminal_size, name, system
from sys import stdout

class Terminal:
    '''
    Terminal class
    '''
    def get_size():
        '''
        Returns the size of the terminal
        output:
            - columns: int
                number of columns
            - lines: int
                number of lines
        '''
        return get_terminal_size().columns, get_terminal_size().lines

    def get_lines():
        '''
        Returns the number of lines of the terminal
        output:
            - lines: int
                number of lines
        '''
        return get_terminal_size().lines

    def get_columns():
        '''
        Returns the number of columns of the terminal
        output:
            - columns: int
                number of columns
        '''
        return get_terminal_size().columns

    def clear():
        '''
        Clears the terminal
        '''
        system('cls' if name in ('nt', 'dos') else 'clear')

    def curser_to_pos1():
        '''
        Moves the curser to the first position
        '''
        for _ in range(self.get_lines() + 2):
            stdout.write("\033[F")


class Matrix:
    '''
    Matrix class
    '''
    def __init__(self):
        self.columns, self.lines = Terminal.get_size()
        self.clear()

    def clear(self):
        '''
        Clears the matrix
        '''
        self.matrix = []

    def refresh(self):
        '''
        Refreshes the matrix
        '''
        self.columns, self.lines = Terminal.get_size()
        self.clear()
        for i in range(self.lines):
            self.matrix.append([])
            for _ in range(self.columns):
                self.matrix[i].append(" ")

    def set_frame(self, x, y, dx, dy, rounded=True, double=False, title=None,
                  alligncenter=True):
        '''
        Sets a frame in the matrix
        input:
            - x: int
                x position of the frame
            - y: int
                y position of the frame
            - dx: int
                width of the frame
            - dy: int
                height of the frame
            - rounded: bool
                if the frame is rounded
            - double: bool
                if the frame is double
            - title: str
                title of the frame
            - alligncenter: bool
                if the title is alligned to the center
        '''
        if double:
            self.set( x, y, "╔")
            self.set(x + dx, y, "╗")
            self.set(x, y + dy, "╚")
            self.set(x + dx, y + dy, "╝")
            for i in range(1, dx):
                self.set(x + i, y, "═")
                self.set(x + i, y + dy, "═")
            for i in range(1, dy):
                self.set(x, y + i, "║")
                self.set(x + dx, y + i, "║")
        else:
            if rounded:
                self.set(x, y, "╭")
                self.set(x + dx, y, "╮")
                self.set(x, y + dy, "╰")
                self.set(x + dx, y + dy, "╯")
            else:
                self.set(x, y, "┌")
                self.set(x + dx, y, "┐")
                self.set(x, y + dy, "└")
                self.set(x + dx, y + dy, "┘")
            for i in range(1, dx):
                self.set(x + i, y, "─")
                self.set(x + i, y + dy, "─")
            for i in range(1, dy):
                self.set(x, y + i, "│")
                self.set(x + dx, y + i, "│")
        if title is not None:
            if alligncenter:
                self.set(x + int(dx / 2) - int(len(title) / 2) - 1, y,
                         "┤" if not double else "╡")
                self.set(x + int(dx / 2) + int(len(title) / 2), y, "├" if
                         not double else "╞")
                self.set_string(x + int(dx / 2) - int(len(title) / 2),
                                y, title)
            else:
                self.set(x + 1, y, "┤" if not double else "╡")
                self.set( x + len(title) + 2, y, "├" if not double else
                         "╞")
                self.set_string(x + 2, y, title)

    def set_square(self, x, y, dx, dy, char):
        '''
        Sets a square in the matrix
        input:
            - x: int
                x position of the square
            - y: int
                y position of the square
            - dx: int
                width of the square
            - dy: int
                height of the square
            - char: str
                character of the square
        '''
        for i in range(dx):
            for j in range(dy):
                self.set(x + i, y + j, char)

    def set(self, x, y, value):
        '''
        Sets a value in the matrix
        input:
            - x: int
                x position of the value
            - y: int
                y position of the value
            - value: str
                value
        '''
        try:
            self.matrix[y][x] = value
        except IndexError:
            pass

    def get(self, x, y):
        '''
        Gets a value in the matrix
        input:
            - x: int
                x position of the value
            - y: int
                y position of the value
        output:
            - value: str
                value
        '''
        return self.matrix[y][x]

    def print(self):
        '''
        Prints the matrix
        '''
        for i in range(self.lines):
            for j in range(self.columns):
                print(self.matrix[i][j], end = "")
            print(end = "" if i < self.lines - 1 else "\r")

    def set_string(self, x, y, chars):
        '''
        Sets a string in the matrix
        input:
            - x: int
                x position of the string
            - y: int
                y position of the string
            - chars: str
                string
        '''
        for i in range(len(chars)):
            self.set(x + i, y, chars[i])

    def set_string_center(self, y, chars):
        '''
        Sets a string in the matrix, alligned to the center
        input:
            - y: int
                y position of the string
            - chars: str
                string
        '''
        self.set_string(int(Terminal.get_columns() / 2 - len(chars) / 2),
                        y, chars)

    def get_matrix(self):
        '''
        Gets the matrix
        output:
            - matrix: list
                matrix
        '''
        return self.matrix

    def add_matrix(self, x, y, matrix):
        '''
        Adds a matrix to the matrix
        input:
            - x: int
                x position of the matrix
            - y: int
                y position of the matrix
            - matrix: list
                matrix
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.set(self, x + j, y + i, matrix[i][j])


if __name__ == "__main__":
    term = Terminal()
    term.set_frame(0, 0, term.get_columns(), term.get_lines(), title="Test",
                   alligncenter=True)
    term.set_string_center(1, "Hello World!")
    term.print()
                