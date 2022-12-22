

from os import get_terminal_size, name, system
from sys import stdout

class Terminal:
    def get_size():
        return get_terminal_size().columns, get_terminal_size().lines

    def get_lines():
        return get_terminal_size().lines

    def get_columns():
        return get_terminal_size().columns

    def clear():
        system('cls' if name in ('nt', 'dos') else 'clear')

    def curser_to_pos1(self):
        for i in range(self.get_lines() + 2):
            stdout.write("\033[F")


class Matrix:
    def __init__(self):
        self.columns, self.lines = Terminal.get_size()
        self.clear(self)

    def clear(self):
        self.matrix = []

    def refresh(self):
        self.columns, self.lines = Terminal.get_size()
        self.clear(self)
        for i in range(self.lines):
            self.matrix.append([])
            for j in range(self.columns):
                self.matrix[i].append(" ")

    def set_frame(self, x, y, dx, dy, rounded=True, double=False, title=None,
                  alligncenter=True):
        if double:
            self.set(self, x, y, "╔")
            self.set(self, x + dx, y, "╗")
            self.set(self, x, y + dy, "╚")
            self.set(self, x + dx, y + dy, "╝")
            for i in range(1, dx):
                self.set(self, x + i, y, "═")
                self.set(self, x + i, y + dy, "═")
            for i in range(1, dy):
                self.set(self, x, y + i, "║")
                self.set(self, x + dx, y + i, "║")
        else:
            if rounded:
                self.set(self, x, y, "╭")
                self.set(self, x + dx, y, "╮")
                self.set(self, x, y + dy, "╰")
                self.set(self, x + dx, y + dy, "╯")
            else:
                self.set(self, x, y, "┌")
                self.set(self, x + dx, y, "┐")
                self.set(self, x, y + dy, "└")
                self.set(self, x + dx, y + dy, "┘")
            for i in range(1, dx):
                self.set(self, x + i, y, "─")
                self.set(self, x + i, y + dy, "─")
            for i in range(1, dy):
                self.set(self, x, y + i, "│")
                self.set(self, x + dx, y + i, "│")
        if title is not None:
            if alligncenter:
                self.set(self, x + int(dx / 2) - int(len(title) / 2) - 1, y,
                         "┤" if not double else "╡")
                self.set(self, x + int(dx / 2) + int(len(title) / 2), y, "├" if
                         not double else "╞")
                self.set_string(self, x + int(dx / 2) - int(len(title) / 2),
                                y, title)
            else:
                self.set(self, x + 1, y, "┤" if not double else "╡")
                self.set(self, x + len(title) + 2, y, "├" if not double else
                         "╞")
                self.set_string(self, x + 2, y, title)

    def set_square(self, x, y, dx, dy, char):
        for i in range(dx):
            for j in range(dy):
                self.set(self, x + i, y + j, char)

    def set(self, x, y, value):
        try:
            self.matrix[y][x] = value
        except IndexError:
            pass

    def get(self, x, y):
        return self.matrix[y][x]

    def print(self):
        for i in range(self.lines):
            for j in range(self.columns):
                print(self.matrix[i][j], end="")
            print(end="" if i < self.lines - 1 else "\r")

    def set_string(self, x, y, chars):
        for i in range(len(chars)):
            self.set(self, x + i, y, chars[i])

    def set_string_center(self, y, chars):
        self.set_string(self, int(Terminal.get_columns() / 2 - len(chars) / 2),
                        y, chars)

    def get_matrix(self):
        return self.matrix

    def add_matrix(self, x, y, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.set(self, x + j, y + i, matrix[i][j])