from algorithm.coding.base32 import Base32

import unittest
import secrets
import base64

class TestBase16(unittest.TestCase) :
    def test_encode(self) -> None :
        for _ in range(100) :
            for i in range(10, 100) :
                random_bytes = secrets.token_bytes(i)
                self.assertEqual(
                    base64.b32encode(random_bytes).decode("utf-8"),
                    Base32.encode(random_bytes)
                )

    def test_decode(self) -> None :
        for _ in range(100) :
            for i in range (10, 100) :
                random_base32_encoded = base64.b32encode(
                    secrets.token_bytes(i)
                ).decode("utf-8")
                self.assertEqual(
                    base64.b32decode(random_base32_encoded),
                    Base32.decode(random_base32_encoded)
                )
