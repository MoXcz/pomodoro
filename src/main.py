from time import sleep


def main():
    start(3600, False)


def start(time, log):
    for i in range(time + 60):
        sleep(1)
        if i % 60 == 0 and log is True:
            print(i / 60)


if __name__ == "__main__":
    main()
