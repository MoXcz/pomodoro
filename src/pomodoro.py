from time import sleep
import argparse
from config import Configuration
from log import update_csv


def set_parser():
    parser = argparse.ArgumentParser(
        prog="pomodoro",
        description="Pomodoro timer for study sessions",
        epilog="A configuration directory is necessary for the command to work",
    )
    parser.add_argument(
        "-c",
        "--config",
        help="set the directory for configuration and log files",
        type=str,
        default=".config",
    )
    return parser


def main():
    args = set_parser().parse_args()
    config = Configuration(args.config)
    start_timer(config)


def start_timer(config):
    log = config.params["log"]
    work_time = int(config.params["work"])
    break_time = int(config.params["break"])
    try:
        print(f"Timer started: {work_time} min")
        timer(work_time * 60, log)
        print(f"Timer complete\nBreak start: {break_time} min")
        timer(break_time * 60, log)
        if log:
            update_csv(config)
    except KeyboardInterrupt:
        print("timer did not complete")


def timer(time, log):
    for i in range(time + 60):
        # sleep(1)
        if i % 60 == 0 and log:
            print(i / 60)


if __name__ == "__main__":
    main()
