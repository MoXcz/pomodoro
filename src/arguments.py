import argparse
from config import configuration_from_ini
import log

file = open("config.ini", "r")
config = configuration_from_ini(file.read())

params = config.params

WORK_TIME = params["work"]
BREAK_TIME = params["break"]
LOG = params["log"]


def setArguments():
    parser = argparse.ArgumentParser(
        prog="pomodoro",
        description="Pomodoro timer for study sessions",
        epilog="...",
    )
    parser.add_argument(
        "-w",
        "--work",
        help="set the time for the work time in pomodoro session",
        type=int,
        default=WORK_TIME,
    )
    parser.add_argument(
        "-b",
        "--break",
        help="set the time for break time in  pomodoro session",
        type=int,
        default=BREAK_TIME,
    )
    parser.add_argument(
        "-l", "--log", help="set to to turn on log", action="store_true"
    )
    parser.add_argument("--file", type=argparse.FileType("w"), default="sessions.csv")
    print(
        f"Arguments were added correctly with default values: \nwork: {WORK_TIME}\nbreak: {BREAK_TIME}\nlog: {LOG}"
    )
    return parser


file.close()
