#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from typing import Any

import pydantic


class Configuration(pydantic.BaseModel):
    """
    Represents the configuration object.
    """

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def save(self, /, **data: Any):
        if 'filepath' not in data:
            raise KeyError("The filepath key was not defined")

    @classmethod
    def load(cls, filepath: str) -> 'Configuration':
        """

        :param filepath:
        :return:
        """
        if filepath is None:
            raise ValueError("The configuration filepath cannot be None")

        return Configuration(filepath=filepath)
