# -*- coding: utf-8 -*-

from snapshottest.unittest import TestCase
from find_route import FindRoute, DEFAULT_CSVFILE


class TestFindRoute(TestCase):

    def test_with_csvfile_not_existent(self):
        with self.assertRaises(FileNotFoundError):
            FindRoute(_origin='GRU', _destination='CDG', _filename='any_csvfile.csv')

    def test_without_origin_parameter(self):
        with self.assertRaises(Exception):
            FindRoute(_destination='CDG')

    def test_without_destination_parameter(self):
        with self.assertRaises(Exception):
            FindRoute(_origin='GRU')

    def test_with_required_parameter(self):
        response = FindRoute(_origin='GRU', _destination='CDG').main()

        self.assertMatchSnapshot(response)

    def test_with_all_parameter(self):
        response = FindRoute(_origin='GRU', _destination='CDG', _filename=DEFAULT_CSVFILE).main()

        self.assertMatchSnapshot(response)
