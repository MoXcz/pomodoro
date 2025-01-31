from time import sleep
from arguments import setArguments
from log import checkCsvFile


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


if __name__ == "__main__":
    main()
