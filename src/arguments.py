import argparse


def setArguments():
    parser = argparse.ArgumentParser(
        prog="pomodoro",
        description="Pomodoro timer for study sessions",
        epilog="...",
    )
    parser.add_argument("start")
    parser.add_argument("time", help="set the time for the pomodoro session", type=int)
    parser.add_argument(
        "-l", "--log", help="set to to turn on log", action="store_true"
    )
    parser.add_argument("--file", type=argparse.FileType("w"))
    return parser
