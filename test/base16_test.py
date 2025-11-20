from algorithm.coding.base16 import Base16

import unittest
import secrets
import base64

class TestBase16(unittest.TestCase) :
    def test_encode(self) -> None :
        for _ in range(100) :
            for i in range(10, 100) :
                random_bytes = secrets.token_bytes(i)
                self.assertEqual(
                    base64.b16encode(random_bytes).decode("utf-8"),
                    Base16.encode(random_bytes)
                )

    def test_decode(self) -> None :
        for _ in range(100) :
            for i in range(10, 100) :
                random_base16_encoded = base64.b16encode(
                    secrets.token_bytes(i)
                ).decode("utf-8")
                self.assertEqual(
                    base64.b16decode(random_base16_encoded),
                    Base16.decode(random_base16_encoded)
                )
