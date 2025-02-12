import os
import configparser




class Configuration:
    def __init__(self, config_dir=".config"):
        self.config_dir = config_dir
        self.set_config_dir()  # set configuration inside /home/user/ (~)
        self.config_file = ""
        self.log_file = ""

    def create_log_file(self):
        if not self.config_dir:
            return
        self.log_file = os.path.join(self.config_dir, "sessions.csv")
        if not os.path.exists(self.log_file):
            print(f"Created: {self.log_file}")
            open(self.log_file, "x")

    def create_config_file_and_dir(self):
        if not self.config_dir:
            return
        pomodoro_dir = os.path.join(self.config_dir, "pomodoro")
        if not os.path.exists(pomodoro_dir):
            print(f"Created: {pomodoro_dir}")
            os.mkdir(pomodoro_dir)
        self.config_dir = pomodoro_dir

        pomodoro_config = os.path.join(pomodoro_dir, "config.ini")
        if not os.path.exists(pomodoro_config):
            print(f"Created: {pomodoro_config}")
            open(pomodoro_config, "x")
        self.config_file = pomodoro_config

    def parse_config_file(self):
        if not self.config_file:
            return
        config = open(self.config_file, "r").read()
        parser = configparser.ConfigParser()
        parser.read_string(config)
        return parser

    def populate_config_file(self):
        sensible_default = """
[files]
input-dir = {{ input }}
output-dir = {{ output }}

[arguments]
work = 25
break = 5
log = 1
"""
        sensible_default = (
            sensible_default.replace("{{ input }}", self.config_file)
            .replace("{{ output }}", self.log_file)
            .strip()
        )
        file = open(self.config_file, "w")
        file.write(sensible_default)

    def set_config_dir(self):
        home = os.path.expanduser("~")
        config_dir = os.path.expandvars("$XDG_CONFIG_HOME")
        if not config_dir or self.config_dir != ".config":
            config_dir = os.path.join(home, self.config_dir)
            print(
                f"XDG_CONFIG_HOME env var not set or \nconfiguration directory specified, config_dir set to: {config_dir}"
            )
        self.config_dir = config_dir
