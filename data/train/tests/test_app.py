"""Tests for app.py."""

from unittest import TestCase

from data.train.app import train

class TestApp(TestCase):
    """Unit Test for app.py."""

    def test_train(self):
        """Test train endpoint."""
        coeff = train()
        self.assertEqual(coeff, "200 OK")
