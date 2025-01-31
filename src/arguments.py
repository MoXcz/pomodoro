import argparse

from config import getConfig


opts = getConfig()
WORK_TIME = opts["work_time"]
LOG = opts["log"]
BREAK_TIME = opts["break_time"]


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
    return parser
