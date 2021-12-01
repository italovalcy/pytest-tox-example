"""Unit test main."""

from unittest import TestCase
from unittest.mock import patch

from src.main import square

class TestMain(TestCase):
    """Class to Unit test square main."""

    def test_square(self):
        """Verify basic call for square function."""
        assert square(4) == 16
