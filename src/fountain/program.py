import json

from fountain.command import ChangeNozzlePressureAndColorFountainCommand


class FountainProgram:
    def __init__(self, commands):
        self.commands = commands

    @staticmethod
    def parse_json(s):
        data = json.loads(s)
        parsers = {
            1: FountainProgram.parse_json_v1
        }

        def unsupported_version_stub(data):
            raise ValueError("Unsupported version '{}', required one of [{}]".format(
                    data['version'], ', '.join(map(str, parsers.keys))))

        return parsers.get(data['version'], unsupported_version_stub)(data)

    @staticmethod
    def parse_json_v1(data):
        assert data['version'] == 1
        return FountainProgram([FountainProgram.parse_json_command_v1(c) for c in data['commands']])

    @staticmethod
    def parse_json_command_v1(command):
        return ChangeNozzlePressureAndColorFountainCommand(command['nozzle'], command['pressure'],
                                                           command['color'], command['time'])
