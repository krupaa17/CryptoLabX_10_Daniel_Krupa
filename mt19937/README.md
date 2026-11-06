
# Assignment 10: MT19937 Stream Cipher and Predictable Token Attack

## Aim
To demonstrate why MT19937 is unsuitable for cryptographic applications by implementing a stream cipher, recovering a weak seed, and predicting timestamp-based reset tokens.

## Concepts Used
- MT19937 Pseudorandom Number Generator
- XOR Stream Cipher
- Known-Plaintext Attack
- Brute-Force Seed Recovery
- Timestamp-Based Token Prediction

## Project Files

| File | Description |
|---|---|
| mt19937_stream_cipher.py | Keystream generation, encryption and decryption |
| seed_recovery.py | 16-bit seed brute-force attack |
| token_prediction.py | Timestamp-based token prediction |
| assignment10.ipynb | Theory, experiments, results and flowcharts |
| token_record.txt | Generated simulated reset token |

## Requirements

Python 3 and NumPy.

Install dependencies:

pip install -r requirements.txt

## Execution

Run from the CryptoLabX root directory:

python -m mt19937.mt19937_stream_cipher

python -m mt19937.seed_recovery

python -m mt19937.token_prediction

## Expected Results

1. Successful encryption and decryption.
2. Recovery of the 16-bit seed.
3. Recovery of the timestamp used for token generation.
4. Successful verification of the generated token.

## Security Conclusion

MT19937 is deterministic and is not cryptographically secure.

Use a CSPRNG such as Python's secrets module for real security-sensitive applications.
