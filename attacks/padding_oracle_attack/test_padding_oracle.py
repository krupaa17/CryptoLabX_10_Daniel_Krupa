import unittest

from .oracle import create_challenge
from .padding_oracle import recover_plaintext


class PaddingOracleAttackTests(unittest.TestCase):
    def test_recovers_plaintext_at_padding_boundaries(self):
        plaintexts = (
            b"",
            b"A",
            b"A" * 15,
            b"A" * 16,
            b"A" * 17,
            bytes(range(32)),
        )
        for plaintext in plaintexts:
            with self.subTest(length=len(plaintext)):
                iv, ciphertext, oracle = create_challenge(plaintext)
                recovered, query_count = recover_plaintext(iv + ciphertext, oracle)
                self.assertEqual(recovered, plaintext)
                self.assertGreater(query_count, 0)

    def test_rejects_incomplete_ciphertext(self):
        with self.assertRaises(ValueError):
            recover_plaintext(b"\x00" * 31, lambda _data: False)


if __name__ == "__main__":
    unittest.main()
