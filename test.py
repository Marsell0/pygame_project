

coords = [[4, 2], [5, 2], [6, 2], [7, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [7, 3], [2, 4], [4, 4], [5, 4], [7, 4], [8, 4], [2, 5], [4, 5], [7, 5], [1, 6], [2, 6], [4, 6], [5, 6], [7, 6], [8, 6], [9, 6], [2, 7], [3, 7], [5, 7], [6, 7], [9, 7], [2, 8], [3, 8], [4, 8], [5, 8], [9, 8], [9, 9]]


class A:
    def __init__(self):
        pass

    def qwe(self, path):
        B.test(path)


class B:
    def __init__(self, path):
        self.c = path
        self.right_path = []

    def test(self, c):
        for i in c:
            self.right_path.append([i[0] * 50 - 25, i[1] * 50 - 25])
        print([self.right_path[0][0], self.right_path[0][1]])


g = A
g.qwe(coords)
