import unittest

import amplitude


class TestModule(unittest.TestCase):

    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        amplitude.write_key = 'testsecret'
        amplitude.on_error = self.failed

    def test_no_write_key(self):
        amplitude.write_key = None
        self.assertRaises(Exception, amplitude.track)

    def test_no_host(self):
        amplitude.host = None
        self.assertRaises(Exception, amplitude.track)

    def test_track(self):
        amplitude.track('userId', 'python module event')
        amplitude.flush()

    def test_flush(self):
        amplitude.flush()
