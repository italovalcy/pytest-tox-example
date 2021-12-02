"""Unit test main."""

from unittest import TestCase
from unittest.mock import patch

from src.main import square


class TestMain(TestCase):
    """Class to Unit test square main."""

    def test_square(self):
        """Verify basic call for square function."""
        self.assertEqual(square(4), 16)

    @patch('numpy.random.randint', return_value=3)
    def test_square_randint(self, *args):
        """Verify square function with no arg."""
        (_) = args
        self.assertEqual(square(), 9)
