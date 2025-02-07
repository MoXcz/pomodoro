from time import sleep
import argparse
from config import Configuration
from log import checkCsvFile


config = Configuration()
config.create_config_file_and_dir()
config.create_log_file()
config.populate_config_file()
params = config.parse_config_file()["arguments"]

WORK_TIME = params["work"]
BREAK_TIME = params["break"]
LOG = params["log"]


def main():
    args = setArguments().parse_args()
    if args.log:
        print("log has been turned on for this session")
        start_timer(args.work, True)
        return
    start_timer(args.work, False)
    if args.file:
        checkCsvFile(args.file)
        args.file.close()


def start_timer(time, log):
    time *= 60
    for i in range(time + 60):
        sleep(1)
        if i % 60 == 0 and log is True:
            print(i / 60)


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
    return parser


if __name__ == "__main__":
    main()
