import unittest

from fountain.command import ChangeNozzlePressureAndColorFountainCommand
from fountain.program import FountainProgram


class TestFountainProgram(unittest.TestCase):
    def test_parse_json(self):
        json = """{
            "version": 1,
            "commands": [
                {
                    "nozzle": 1,
                    "pressure": 42,
                    "color": "green",
                    "time": 5
                },
                {
                    "nozzle": 2,
                    "pressure": 3.14,
                    "color": "red",
                    "time": 2
                },
                {
                    "nozzle": 5,
                    "pressure": 0,
                    "color": "yellow",
                    "time": 10
                }
            ]
        }"""

        program = FountainProgram.parse_json(json)

        self.assertListEqual([ChangeNozzlePressureAndColorFountainCommand(1, 42, 'green', 5),
                              ChangeNozzlePressureAndColorFountainCommand(2, 3.14, 'red', 2),
                              ChangeNozzlePressureAndColorFountainCommand(5, 0, 'yellow', 10)],
                             program.commands)
