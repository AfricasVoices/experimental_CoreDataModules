import unittest

from core_data_modules.util import SHAUtils


class TestSHAUtils(unittest.TestCase):
    def test_sha_string(self):
        self.assertEqual(
            SHAUtils.sha_string("test"),
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        )

        self.assertEqual(
            SHAUtils.sha_string(""),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        )

    def test_create_hash_id(self):
        self.assertEqual(SHAUtils.create_hash_id("test"), "7271004174")
        self.assertEqual(SHAUtils.create_hash_id(""), "9372699152")
        self.assertEqual(SHAUtils.create_hash_id("+2212345123123"), "1517694669")