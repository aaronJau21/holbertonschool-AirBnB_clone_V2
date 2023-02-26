#!/usr/bin/python3
"""Test for class FileStorage."""


import unittest
import models

FileStorage = models.file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage docs."""

    def test_doc_module(self):
        """Test moduel documentation."""
        actual = models.file_storage.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = FileStorage.__doc__
        self.assertIsNotNone(actual)

    def test__file_path(self):
        """Test for class private attribute __file_path."""
        actual = FileStorage.__file_path
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main
