from algorithm.coding.base64 import Base64

import unittest
import secrets
import base64

class TestBase16(unittest.TestCase) :
    def test_encode(self) -> None :
        for _ in range(100) :
            for i in range(10, 100) :
                random_bytes = secrets.token_bytes(i)
                self.assertEqual(
                    base64.b64encode(random_bytes).decode("utf-8"),
                    Base64.encode(random_bytes)
                )

    def test_decode(self) -> None :
        for _ in range(100) :
            for i in range (10, 100) :
                random_base64_encoded = base64.b64encode(
                    secrets.token_bytes(i)
                ).decode("utf-8")
                self.assertEqual(
                    base64.b64decode(random_base64_encoded),
                    Base64.decode(random_base64_encoded)
                )
