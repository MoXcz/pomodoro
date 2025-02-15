# Pomodoro

This program is a CLI implementation of the Pomodoro technique that reads work
and break times from a configuration file (default in `$HOME/.config/pomodoro`).

It also stores each individual session inside a `csv` file
(default in `$HOME/.config/pomodoro/sessions.csv`)

For more info on the Pomodoro technique read [here](https://en.wikipedia.org/wiki/Pomodoro_Technique)

## Installation

- This project uses Python and thus the Python interpreter is needed, click
  [here](https://www.python.org/downloads/) for more information on how to install
  it.

To start first clone the repository:

```sh
git clone https://github.com/MoXcz/pomodoro.git --depth 1
```

After that just run the program using the Python interpreter:

```python
./pomodoro
```

## Use

This program accepts a single optional argument that defines the configuration directory:

```sh
./pomodoro -c .config
```

This will create the configuration directory inside `$HOME/.config` with a
`sessions.csv` file for logging and `config.ini` for configuration.
