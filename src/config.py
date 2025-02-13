import os
import configparser




class Configuration:
    def __init__(self, config_dir=".config"):
        self.config_dir = config_dir
        self.set_config_directory()  # set configuration inside /home/user/config_dir (~)
        self.log_file = os.path.join(self.config_dir, "sessions.csv")
        self.config_file = os.path.join(self.config_dir, "config.ini")
        self.initialize_configuration()
        self.params = self.load_config()["arguments"]

    def initialize_configuration(self):
        if os.path.exists(self.config_dir):
            return

        while True:
            user_input = (
                input(
                    f"Do you want to create config.ini at {self.config_dir}? [yes or no]: "
                )
                .strip()
                .lower()
            )

            if user_input in {"yes", "y"}:
                self.create_config_file_and_dir()
                self.create_log_file()
                self.populate_config_file()
                break
            elif user_input in {"no", "n"}:
                print("Nothing happened, exiting")
                exit(1)

    def create_log_file(self):
        if not self.config_dir or os.path.exists(self.log_file):
            return

        print(f"Creating log file: {self.log_file}")
        open(self.log_file, "x")

    def create_config_file_and_dir(self):
        if not self.config_dir or os.path.exists(self.log_file):
            return

        print(f"Creating config directory: {self.config_dir}")
        os.mkdir(self.config_dir)

        if not os.path.exists(self.config_file):
            print(f"Creating config file: {self.config_file}")
            open(self.config_file, "x")

    def load_config(self):
        parser = configparser.ConfigParser()
        if not os.path.exists(self.config_file):
            return parser
        parser.read(self.config_file)
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

    def set_config_directory(self):
        home = os.path.expanduser("~")
        config_dir = os.path.expandvars("$XDG_CONFIG_HOME")
        if not config_dir or self.config_dir != ".config":
            config_dir = os.path.join(home, self.config_dir)
        config_dir = os.path.join(config_dir, "pomodoro")
        self.config_dir = config_dir
