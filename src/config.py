import os
import configparser

dir = os.path.dirname(__file__)


class Configuration:
    def __init__(self, input_dir, output_dir, params) -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.params = params


def configuration_from_dict(details):
    files = Configuration(
        details["files"]["input-dir"],
        details["files"]["output-dir"],
        details["arguments"],
    )
    return files


def configuration_from_ini(data):
    parser = configparser.ConfigParser()
    parser.read_string(data)
    return configuration_from_dict(parser)


file = open("config.ini", "r")
config = configuration_from_ini(file.read())
