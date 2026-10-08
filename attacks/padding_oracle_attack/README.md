# Assignment 7: AES-CBC Padding Oracle Attack

## Run

Install the AES library if it is not already available:

```text
python -m pip install cryptography
```

Run the demonstration from the project root:

```text
python -m attacks.padding_oracle_attack.main
```

An alternative plaintext can be supplied in a file:

```text
python -m attacks.padding_oracle_attack.main --input path\to\plaintext.bin
```

The challenge generator creates a fresh key and IV for each run. The key stays
inside the oracle's closure; the attack receives only the IV, ciphertext, and a
function that reports whether PKCS#7 padding is valid. The generic attack is in
`padding_oracle.py`; it does not import or inspect the challenge generator.

## How the attack works

AES-CBC decrypts a ciphertext block `C[i]` as `D(K, C[i]) XOR C[i-1]`, where
`C[0]` is the IV. Changing a byte of the preceding block therefore changes the
corresponding plaintext byte in the target block by the same XOR difference.
AES has a 16-byte block size. PKCS#7 fills the last block with `n` bytes each
equal to `n`, including a full block of `0x10` bytes when the plaintext already
ends on a block boundary.

Starting at the last byte, the attack changes the previous block until the
oracle accepts padding. It then repeats for padding values `0x02` through
`0x10`, preserving already-recovered suffix bytes. This obtains the intermediate
AES decryption bytes, which are XORed with the original preceding block to
recover plaintext. The attack confirms one-byte padding candidates to avoid
mistaking an existing longer padding suffix for a match.

## Analysis record

For the built-in sample, the program prints the recovered plaintext and exact
number of oracle calls on each run. The query count varies because each run
uses fresh random AES key and IV values; for a block the search takes at most
256 candidate queries per byte, plus a confirmation query in the one-byte case.
One recorded run recovered:

```text
b'Padding oracles reveal plaintext one byte at a time without the AES key.'
Oracle queries: 10437
```

## Prevention

Do not expose distinguishable padding errors, response bodies, or timing for
decryption failures. Prefer authenticated encryption such as AES-GCM or
ChaCha20-Poly1305, and verify the authentication tag before releasing any
plaintext. If legacy CBC must be used, authenticate the IV and ciphertext with
an encrypt-then-MAC construction and verify the MAC in constant time before
decrypting or checking padding. Return one indistinguishable failure for all
invalid inputs.

## Tests

```text
python -m unittest attacks.padding_oracle_attack.test_padding_oracle
```
