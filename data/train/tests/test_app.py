"""Tests for app.py."""

from unittest import TestCase

import train.app

class TestApp(TestCase):
    """Unit Test for app.py."""

    def test_train(self):
        """Test train endpoint."""
        coeff = train()
        self.assertEqual(coeff, "200 OK")
