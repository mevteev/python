class Level:
    def __init__(self, name, points, ghosts):
        self.name = name
        self.points = points
        self.ghosts = ghosts

    def __str__(self):
        res = 'Name: ' + self.name + '\n'
        res += 'Points:\n'
        for point in self.points:
            res += str(point) + '\n'
        res += 'Ghosts:\n'
        for ghost in self.ghosts:
            res += str(ghost) + '\n'
        return res

class Ghost:
    def __init__(self, color, coordinates):
        self.color = color
        self.coordinates = coordinates

    def __str__(self):
        return self.color + " " + str(self.coordinates)

class Pinky(Ghost):
    def __init__(self, coordinates):
        Ghost.__init__(self, "pink", coordinates)

class Clyde(Ghost):
    def __init__(self, coordinates):
        Ghost.__init__(self, "orange", coordinates)
    

class Blinky(Ghost):
    def __init__(self, coordinates):
        Ghost.__init__(self, "black", coordinates)


class Inky(Ghost):
    def __init__(self, coordinates):
        Ghost.__init__(self, "blue", coordinates)
    


def read_properties(filename):
    with open(filename) as f:
        l = [line.split("=") for line in f.readlines()]
    print(l)
    

def main():
    read_properties("pacman.properties")
    
def test():
    point1 = (107,211)
    point2 = (231, 313)
    point3 = (471, 562)
    point4 = (569, 647)
    points = [point1, point2, point3, point4]

    ghost1 = Blinky((10, 20))
    ghost2 = Pinky((21, 32))
    ghost3 = Inky((41, 57))
    ghost4 = Clyde((17, 83))

    ghosts = [ghost1, ghost2, ghost3, ghost4]


    level = Level("First level", points, ghosts)


    print(level)


if __name__ == "__main__":
    main()   
