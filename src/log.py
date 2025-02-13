import os
import csv


def initialize_csv(filepath):
    with open(filepath, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Work Time", "Break Time"])


def update_csv(config):
    params = config.load_config()["arguments"]
    filepath = config.log_file

    if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
        initialize_csv(filepath)
        return

    work_time = params["work"]
    break_time = params["break"]

    with open(filepath, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([work_time, break_time])

    print(
        f"Added entry: Work Time = {work_time}, Break Time = {break_time} at {filepath}"
    )
