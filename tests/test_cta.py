import unittest

import pandas
import pandas.util.testing as pdt

import cta.cta as mod_ut

class TestCTA(unittest.TestCase):
    def setUp(self):
        df = pandas.DataFrame({
            'stop_id': [0, 1, 2],
            'routes': ['A,B', 'A', 'A'],
            'on_street': ['foo', 'bar', 'baz']
        })
        self.stop_route_manager = mod_ut.StopRouteManager(df)

    def test_get_normalized_route_stops(self):
        """ Asserts that the denormalization logics works properly """
        result = self.stop_route_manager._get_normalized_route_stops()
        expected = pandas.DataFrame({
            'stop_id': [0, 0, 1, 2],
            'route': ['A', 'B', 'A', 'A']
        })
        pdt.assert_frame_equal(result.sort_index(axis=1),
            expected.sort_index(axis=1))

    def test_get_busiest_stop(self):
        result = self.stop_route_manager.get_busiest_stop()
        expected = 0
        self.assertEqual(result, expected)

    def test_get_longest_route(self):
        result = self.stop_route_manager.get_longest_route()
        expected = 'A'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
