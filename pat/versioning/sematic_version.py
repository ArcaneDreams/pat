#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from __future__ import annotations


class SemanticVersion(object):
    """
    Defines a semantic version as defined by the conventions outlined here
    https://semver.org/
    """

    def __init__(self, major: int, minor: int, patch: int):
        """

        :type major: int
        :type minor: int
        :type patch: int
        """
        assert isinstance(major, int)
        assert isinstance(minor, int)
        assert isinstance(patch, int)
        self._version = [major, minor, patch]

    @property
    def major(self) -> int:
        """
        The major version number
        :return:
        """
        return self._version[0]

    @property
    def minor(self) -> int:
        """
        The minor version number
        :return:
        """
        return self._version[1]

    @property
    def patch(self) -> int:
        """
        The patch version number
        :return:
        """
        return self._version[2]

    def __eq__(self, other: SemanticVersion):
        """

        :type other: SemanticVersion
        """
        return self._version == other._version

    def __ne__(self, other: SemanticVersion):
        """

        :type other: SemanticVersion
        """
        pass

    def __str__(self):
        """
        The string representation of the semantic version
        :return:
        """
        return f"{self.major}.{self.minor}.{self.patch}"

    def __lt__(self, other: SemanticVersion):
        """

        :type other: SemanticVersion
        """
        if not other:
            raise ValueError('Cannot compare empty SemanticVersion')

        for index in len(self._version):
            if self._version[index] < other._version[index]:
                return True

        return False

    def __gt__(self, other: SemanticVersion):
        """

        :type other: SemanticVersion
        """
        if not other:
            raise ValueError('Cannot compare empty SemanticVersion')

        for index in len(self._version):
            if self._version[index] > other._version[index]:
                return True

        return False
