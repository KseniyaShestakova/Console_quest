import random
import sys


class Field:
    end_of_the_game = False
    victory = False
    size = 4
    score = 0
    matrix = [[-1, -1, -1, -1],
              [-1, -1, -1, -1],
              [-1, -1, -1, -1],
              [-1, -1, -1, -1]]

    def __init__(self, sz, matrix_list=None):
        self.size = sz
        self.score = 0
        if matrix_list is None:
            matrix_list = [-1] * self.size
            for i in range(self.size):
                matrix_list[i] = ([-1] * self.size)
        self.matrix = matrix_list

    def is_empty(self, x, y):
        return self.matrix[x][y] == -1

    def get(self, x, y):
        return self.matrix[x][y]

    def set(self, x, y, val):
        self.matrix[x][y] = val

    def _shift_left(self, x):
        # сдвигаем строку влево
        current_list = []
        for i in range(self.size):
            if not self.is_empty(x, i):
                current_list.append(self.get(x, i))
        counter = 0
        result_list = []
        while counter < len(current_list) - 1:
            if current_list[counter] == current_list[counter + 1]:
                result_list.append(2 * current_list[counter])
                self.score += 2 * current_list[counter]
                counter += 2
            else:
                result_list.append(current_list[counter])
                counter += 1
        if counter == len(current_list) - 1:
            result_list.append(current_list[counter])
        self.matrix[x] = result_list + [-1] * (self.size - len(result_list))

    def _shift_right(self, x):
        current_list = []
        for i in range(self.size):
            if not self.is_empty(x, i):
                current_list.append(self.get(x, i))
        # print(current_list)
        counter = len(current_list) - 1
        result_list = []
        while counter > 0:
            if current_list[counter] == current_list[counter - 1]:
                result_list.insert(0, 2 * current_list[counter])
                self.score += 2 * current_list[counter]
                counter -= 2
            else:
                result_list.insert(0, current_list[counter])
                counter -= 1
        if counter == 0:
            result_list.insert(0, current_list[counter])
        # print(result_list)
        self.matrix[x] = [-1] * (self.size - len(result_list)) + result_list

    def _shift_up(self, y):
        current_list = []
        for i in range(self.size):
            if not self.is_empty(i, y):
                current_list.append(self.get(i, y))
        counter = 0
        result_list = []

        while counter < len(current_list) - 1:
            if current_list[counter] == current_list[counter + 1]:
                result_list.append(2 * current_list[counter])
                self.score += 2 * current_list[counter]
                counter += 2
            else:
                result_list.append(current_list[counter])
                counter += 1
        if counter == len(current_list) - 1:
            result_list.append(current_list[counter])
        result_list += [-1] * (self.size - len(result_list))
        for i in range(self.size):
            self.set(i, y, result_list[i])

    def _shift_down(self, y):
        current_list = []
        for i in range(self.size):
            if not self.is_empty(i, y):
                current_list.append(self.get(i, y))
        counter = len(current_list) - 1
        result_list = []
        while counter > 0:
            if current_list[counter] == current_list[counter - 1]:
                result_list.insert(0, 2 * current_list[counter])
                self.score += 2 * current_list[counter]
                counter -= 2
            else:
                result_list.insert(0, current_list[counter])
                counter -= 1
        if counter == 0:
            result_list.insert(0, current_list[counter])
        result_list = [-1] * (self.size - len(result_list)) + result_list
        for i in range(self.size):
            self.set(i, y, result_list[i])

    def shift_left(self):
        for x in range(self.size):
            self._shift_left(x)

    def shift_right(self):
        for x in range(self.size):
            self._shift_right(x)

    def shift_up(self):
        for y in range(self.size):
            self._shift_up(y)

    def shift_down(self):
        for y in range(self.size):
            self._shift_down(y)

    def show(self, need_cleaning_up):
        if need_cleaning_up:
            for i in range(self.size + 2):
                sys.stdout.write("\x1b[1A\x1b[2K")
        print("score: " + str(self.score))
        for i in range(self.size):
            string = ""
            for j in range(self.size):
                if self.get(i, j) == 1:
                    string += "\u001b[32m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 2:
                    string += "\u001b[36m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 4:
                    string += "\u001b[35m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 8:
                    string += "\u001b[31m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 16 or self.get(i, j) == 32:
                    string += "\u001b[32;1m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 64 or self.get(i, j) == 2048:
                    string += "\u001b[35;1m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 128 or self.get(i, j) == 256:
                    string += "\u001b[33m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == 512 or self.get(i, j) == 1024:
                    string += "\u001b[33;1m" + str(self.get(i, j)) + "\u001b[0m" + " " * (5 - len(str(self.get(i, j))))
                    continue
                if self.get(i, j) == -1:
                    string += "*" + " " * 4
                    continue

            print(string)

    def next(self, i, j):
        if i == self.size - 1 and j == self.size - 1:
            return [0, 0]
        if j != self.size - 1:
            return [i, j + 1]
        else:
            return [i + 1, 0]

    def check_victory(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.get(i, j) == 2048:
                    self.victory = True
                    self.end_of_the_game = True

    def add_point(self):
        additive = random.randint(1, 2)
        cells_examined = 0
        empty_cells_list = []
        cell = [0, 0]
        while cells_examined < self.size * self.size + 1:
            if self.get(cell[0], cell[1]) == -1:
                empty_cells_list.append(cell)
            cells_examined += 1
            cell = self.next(cell[0], cell[1])
        if len(empty_cells_list) == 0:
            self.end_of_the_game = True
            return
        position = random.randint(0, len(empty_cells_list) - 1)
        self.set(empty_cells_list[position][0], empty_cells_list[position][1], additive)

    def play(self):
        need_cleaning_up = False
        while True:
            self.check_victory()
            self.add_point()
            if self.end_of_the_game:
                print("End!")
                break
            self.show(need_cleaning_up)
            key = input()
            if key == 'a':
                self.shift_left()
            if key == 'd':
                self.shift_right()
            if key == 'w':
                self.shift_up()
            if key == 's':
                self.shift_down()
            need_cleaning_up = True
            self.show(need_cleaning_up)
            if key == "esc":
                break
            print("score: " + str(self.score))

