from pathlib import Path

import yaml


class PolicyLoader:

    def __init__(self):

        self.path = (
            Path(__file__)
            .parent
            / "rules"
            / "default.yaml"
        )

    def load(self):

        with open(self.path, "r") as file:
            return yaml.safe_load(file)