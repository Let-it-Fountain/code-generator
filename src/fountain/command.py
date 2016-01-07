from fountain.color import Color
from utils import CommonEqualityMixin


class BaseFountainCommand:
    pass


class ChangeNozzlePressureAndColorFountainCommand(CommonEqualityMixin, BaseFountainCommand):
    def __init__(self, nozzle, pressure, color, time):
        self.nozzle = nozzle
        self.pressure = pressure
        self.color = Color(color)
        self.time = time
