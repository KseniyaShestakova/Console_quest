import random


class Field:
    end_of_the_game = False
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

    def show(self):
        print("------------------------------------------------------")
        for i in range(self.size):
            string = ""
            for j in range(self.size):
                if self.get(i, j) != -1:
                    string += str(self.get(i, j)) + " " * (5 - len(str(self.get(i, j))))
                else:
                    string += "*" + " " * 4

            print(string)

    def next(self, i, j):
        if i == self.size - 1 and j == self.size - 1:
            return [0, 0]
        if j != self.size - 1:
            return [i, j + 1]
        else:
            return [i + 1, 0]

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

        while True:
            self.add_point()
            if self.end_of_the_game:
                print("End!")
                break
            self.show()
            choice = input()
            if choice == "left":
                self.shift_left()
            if choice == "right":
                self.shift_right()
            if choice == "up":
                self.shift_up()
            if choice == "down":
                self.shift_down()
            self.show()
            if choice == "break":
                break
            print("score: " + str(self.score))


obj = Field(5)
obj.play()
