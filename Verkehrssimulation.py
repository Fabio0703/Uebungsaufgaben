import math

from unicodedata import east_asian_width


class Road:
    def __init__(self, topology_file):
        self.load_topology(topology_file)
    def load_topology(self, topology_file):
        with open(topology_file, 'r') as file:
            self.topology = [line.strip for line in file]
class Car:
    def __init__(self, start_position, direction):
        self.position = start_position
        self.direction = direction
        self.speed = 0.0
    def accelerate(self):
        self.speed = min(self.speed + 0.2, 1) #min(arg1,arg2) vergleicht die Werte und gibt den kleinsten zurück. Sicherstellung, dass 1 nicht überschritten wird.
    def decelerate(self):
        self.speed = max(self.speed / 2, 0.1) #Minimalgeschwindigkeit bei 0.1; stellt somit sicher, dass die Geschwindigkeit immer min. 0.1 beträgt
    def move(self):
        self.position += math.ceil(self.speed) #aufrunden mittels .ceil

def detect_crash(car1,car2):
    return car1.position == car2.position
def simulate (road, car1, car2):
    while True:
        car1.accelerate()
        car2.accelerate()

        if car1.position >= len(road.topology):
            car1.position = len(road.topology) - 1
        if car2.position >= len(road.topology):
            car2.position = len(road.topology) - 1

        if road.topology[car1.position] == 'curve':
            car1.decelerate()
        if road.topology[car2.position] == 'curve':
            car2.decelerate()
        car1.move()
        car2.move()
        if car1.position >= len(road.topology):
            car1.position = len(road.topology) - 1
        if car2.position >= len(road.topology):
            car2.position = len(road.topology) - 1

        if detect_crash(car1,car2):
            print(f"An der Position {car1.position} kam es zu einem Unfall! ")
            break

road = Road('topology.txt')
car1 = Car(start_position=0, direction='east')
car2 = Car(start_position=len(road.topology)-1, direction='west')

simulate(road, car1, car2)