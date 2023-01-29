class Grid:
    width = 2
    height = 2
    length = 4
    array = []
    initiator = None

    def __init__(self, width: int, height: int, initiator: any = None):
        self.width = width
        self.height = height
        self.length = width * height
        self.array = [initiator] * self.length
        self.initiator = initiator

    def get(self, x: int, y: int):
        if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
            return None
        return self.array[x + (y * self.width)]

    def set(self, x: int, y: int, value: any):
        if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
            return
        self.array[x + (y * self.width)] = value

height, width = map(int, input().split(' '))
string = input()

# height = 5
# width = 6
# string = "SoftUni"

grid = Grid(width, height, '-')

i = 0

for y in range(height):
    if y%2 == 0:
        for x in range(width):
            grid.set(x, y, string[i])
            i += 1
            if i > len(string)-1: i = 0
    else:
        for x in range(width-1, -1, -1):
            grid.set(x, y, string[i])
            i += 1
            if i > len(string)-1: i = 0

for y in range(height):
    for x in range(width):
        print(grid.get(x, y), end='')
    print('')