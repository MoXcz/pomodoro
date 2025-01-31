import subprocess


def getConfig():
    opts = {}
    options = (
        subprocess.run(["lua", "./lua/parse.lua"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
        .split("\n")
    )

    for opt in options:
        opt = opt.split("=")
        opts[opt[0]] = opt[1]

    return opts
