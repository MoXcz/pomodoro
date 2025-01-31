import os
import csv


def checkCsvFile(file):
    if os.stat(file.name).st_size == 0:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Name", "Age"])


def csvParser(filename):
    if not filename:
        raise FileNotFoundError("The file could not be opened")
    csv_writer = csv.writer(filename)
    csv_writer.writerow(["Name", "Age"])
