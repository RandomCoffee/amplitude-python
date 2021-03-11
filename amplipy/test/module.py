import unittest

import amplipy


class TestModule(unittest.TestCase):

    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        amplipy.write_key = 'testsecret'
        amplipy.on_error = self.failed

    def test_no_write_key(self):
        amplipy.write_key = None
        self.assertRaises(Exception, amplipy.track)

    def test_no_host(self):
        amplipy.host = None
        self.assertRaises(Exception, amplipy.track)

    def test_track(self):
        amplipy.track('userId', 'python module event')
        amplipy.flush()

    def test_flush(self):
        amplipy.flush()
