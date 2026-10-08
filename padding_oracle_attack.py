"""
Padding Oracle Attack - AES-CBC Decryption without Key
Demonstrates how a padding oracle vulnerability can recover plaintext
from an AES-CBC encrypted message without knowing the encryption key.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import sys


class PaddingOracleAttack:
    """
    Implements a Padding Oracle Attack against AES-CBC encryption.
    
    Theory:
    - AES-CBC encrypts plaintext blocks using the previous ciphertext block as IV
    - PKCS#7 padding adds bytes to make plaintext a multiple of block size
    - A padding oracle tells us if decryption produced valid padding
    - We can exploit this to recover plaintext byte-by-byte
    """
    
    def __init__(self, block_size=16):
        """Initialize the attack handler."""
        self.block_size = block_size
        self.oracle_queries = 0
        
    def padding_oracle(self, ciphertext, key):
        """
        Padding Oracle Function:
        Returns True if decrypted ciphertext has valid PKCS#7 padding.
        
        In a real-world scenario, this would be a remote service that:
        - Decrypts the ciphertext
        - Checks if padding is valid
        - Returns True/False (or different responses like 200/400 HTTP)
        
        Args:
            ciphertext: The encrypted bytes
            key: The secret key (used only by oracle, not the attacker)
            
        Returns:
            bool: True if padding is valid, False otherwise
        """
        self.oracle_queries += 1
        
        try:
            # Use a fixed IV of zeros for consistency
            iv = bytes(self.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(ciphertext)
            
            # Check if PKCS#7 padding is valid
            try:
                unpad(plaintext, self.block_size)
                return True
            except ValueError:
                return False
        except Exception:
            return False
    
    def recover_plaintext_block(self, ciphertext_block, previous_ciphertext_block, key):
        """
        Recover a single plaintext block using padding oracle attack.
        
        Algorithm:
        1. Start from the last byte (rightmost)
        2. Modify the previous ciphertext block byte by byte
        3. Query the oracle to find values that produce valid padding
        4. Use XOR relationship: P[i] = C[i-1]' XOR pad_value XOR C[i-1]
        5. Repeat for all bytes from right to left
        
        Args:
            ciphertext_block: The block we want to decrypt
            previous_ciphertext_block: The IV or previous ciphertext block
            key: The secret key (for oracle only)
            
        Returns:
            bytes: Recovered plaintext block
        """
        plaintext_block = bytearray(self.block_size)
        
        # Process bytes from right to left (last byte first)
        for position in range(self.block_size - 1, -1, -1):
            # Padding value we're targeting (1, 2, 3, ..., 16)
            padding_value = self.block_size - position
            
            # Try all possible byte values (0-255)
            for byte_value in range(256):
                # Create modified previous ciphertext block
                modified_prev = bytearray(previous_ciphertext_block)
                
                # Set the current byte to our test value
                modified_prev[position] = byte_value
                
                # For already recovered bytes, XOR them to produce correct padding
                for i in range(position + 1, self.block_size):
                    modified_prev[i] = (previous_ciphertext_block[i] ^ 
                                       plaintext_block[i] ^ padding_value)
                
                # Query the oracle
                test_ciphertext = bytes(modified_prev) + ciphertext_block
                
                if self.padding_oracle(test_ciphertext, key):
                    # Found valid padding!
                    # P[position] = modified_byte XOR padding_value XOR C_prev[position]
                    plaintext_block[position] = (byte_value ^ padding_value ^ 
                                               previous_ciphertext_block[position])
                    break
        
        return bytes(plaintext_block)
    
    def attack(self, ciphertext, iv, key):
        """
        Execute the padding oracle attack to recover plaintext.
        
        Args:
            ciphertext: The AES-CBC encrypted message
            iv: The initialization vector used for encryption
            key: The secret key (for oracle only)
            
        Returns:
            str: Recovered plaintext
        """
        self.oracle_queries = 0
        
        # Split ciphertext into blocks
        blocks = [ciphertext[i:i+self.block_size] 
                 for i in range(0, len(ciphertext), self.block_size)]
        
        plaintext = b''
        
        # First block uses IV as previous
        previous = iv
        
        print(f"\n[*] Starting Padding Oracle Attack")
        print(f"[*] Total ciphertext blocks: {len(blocks)}")
        print(f"[*] Block size: {self.block_size} bytes\n")
        
        # Recover each block
        for block_num, block in enumerate(blocks):
            print(f"[>] Recovering block {block_num + 1}/{len(blocks)}...", end=" ")
            sys.stdout.flush()
            
            recovered_block = self.recover_plaintext_block(block, previous, key)
            plaintext += recovered_block
            previous = block
            
            print(f"Done (Queries so far: {self.oracle_queries})")
        
        # Remove PKCS#7 padding
        try:
            plaintext = unpad(plaintext, self.block_size)
        except ValueError:
            print("[!] Warning: Padding removal failed, returning raw plaintext")
        
        return plaintext


def demo_attack():
    """Demonstrate the padding oracle attack."""
    
    print("=" * 70)
    print("PADDING ORACLE ATTACK - AES-CBC DECRYPTION")
    print("=" * 70)
    
    # Step 1: Setup (Simulator has the key, Attacker doesn't)
    print("\n[SETUP PHASE]")
    print("-" * 70)
    
    key = get_random_bytes(16)  # 128-bit AES key
    iv = get_random_bytes(16)   # Random IV
    
    # Original plaintext
    plaintext = b"The secret is: Padding Oracle Attacks are powerful!"
    print(f"[Simulator] Plaintext: {plaintext.decode()}")
    print(f"[Simulator] Key: {key.hex()} (HIDDEN FROM ATTACKER)")
    print(f"[Simulator] IV: {iv.hex()}")
    
    # Encrypt the plaintext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, 16))
    
    print(f"\n[Simulator] Encrypted ciphertext: {ciphertext.hex()}")
    print(f"[Simulator] Ciphertext length: {len(ciphertext)} bytes")
    
    # Step 2: Attack Phase (Attacker only knows ciphertext and IV)
    print("\n[ATTACK PHASE]")
    print("-" * 70)
    print("[Attacker] I have: Ciphertext + IV + Access to Padding Oracle")
    print("[Attacker] I DON'T have: The encryption key")
    
    attack = PaddingOracleAttack()
    recovered_plaintext = attack.attack(ciphertext, iv, key)
    
    # Step 3: Results
    print("\n[RESULTS]")
    print("-" * 70)
    print(f"[✓] Recovered plaintext: {recovered_plaintext.decode()}")
    print(f"[✓] Match: {recovered_plaintext == plaintext}")
    print(f"[✓] Total oracle queries used: {attack.oracle_queries}")
    
    return attack.oracle_queries


def main():
    """Run the padding oracle attack demonstration."""
    
    # Run the attack
    oracle_queries = demo_attack()
    
    # Analysis and Explanation
    print("\n[ANALYSIS & EXPLANATION]")
    print("=" * 70)
    
    print("""
1. HOW AES-CBC WORKS:
   - Divides plaintext into 16-byte blocks
   - Each block is XORed with previous ciphertext (or IV for first block)
   - Then encrypted with AES
   - Formula: C[i] = AES_encrypt(P[i] XOR C[i-1])

2. PKCS#7 PADDING:
   - If plaintext is not multiple of 16 bytes, padding is added
   - Padding value = number of padding bytes (1-16)
   - Example: 5 bytes of padding → each byte is 0x05
   - Valid padding means the last N bytes all equal N

3. THE PADDING ORACLE:
   - A function that returns True/False for valid padding
   - Doesn't reveal decrypted plaintext
   - In real world: error messages, HTTP 200 vs 400, timing differences

4. THE ATTACK MECHANISM:
   - Modify previous ciphertext block byte by byte
   - Query oracle for each modification
   - When oracle returns True, we found valid padding
   - Use XOR relationship to recover plaintext byte
   
   Key insight:
   P[i] = C'[i-1] XOR padding_value XOR C_original[i-1]
   
   Where C'[i-1] is the modified previous ciphertext block

5. WHY IT WORKS:
   - AES-CBC: P = AES_decrypt(C) XOR C_prev
   - If we control C_prev, we control the plaintext XOR result
   - By testing different C_prev values, we can make any plaintext appear valid
   - The oracle reveals when our guess produces valid padding

6. ORACLE QUERIES ANALYSIS:
   """)
    
    block_size = 16
    blocks_count = 4  # Typical for demo
    queries_per_byte = 256  # Worst case
    expected_queries = blocks_count * block_size * queries_per_byte
    
    print(f"   - Block size: {block_size} bytes")
    print(f"   - Expected blocks: {blocks_count}")
    print(f"   - Worst case per byte: {queries_per_byte} queries")
    print(f"   - Expected total (worst): {expected_queries}")
    print(f"   - Actual queries used: {oracle_queries}")
    print(f"   - Efficiency: {(oracle_queries / expected_queries * 100):.2f}% of worst case")

    print("""
7. SECURITY RECOMMENDATIONS TO PREVENT PADDING ORACLE ATTACKS:

   a) Use AUTHENTICATED ENCRYPTION:
      - Use AES-GCM or ChaCha20-Poly1305 instead of CBC
      - These provide both confidentiality and authenticity
      
   b) USE CONSTANT-TIME COMPARISON:
      - Compare padding without early exit
      - Prevent timing side-channel leaks
      
   c) FAIL SECURELY:
      - Don't distinguish between "bad padding" and "bad MAC"
      - Use a single error response for any decryption failure
      
   d) USE AUTHENTICATED ENCRYPTION WITH ASSOCIATED DATA (AEAD):
      - Encrypt-then-MAC pattern
      - Verify MAC before attempting to decrypt
      
   e) DEPRECATED MODES:
      - Never use ECB or CBC mode with untrusted input
      - Always prefer AEAD modes (GCM, ChaCha20-Poly1305)
      
   f) IMPLEMENTATIONS:
      - Use cryptographic libraries properly
      - Don't implement encryption yourself
      - Keep libraries updated

8. REAL-WORLD IMPACT:
   - SSL/TLS (pre-1.2): Vulnerable to padding oracle attacks
   - Various web applications with custom crypto
   - Mobile banking apps with weak encryption
   - IoT devices with outdated crypto libraries
    """)
    
    print("\n" + "=" * 70)
    print("ATTACK COMPLETE - PLAINTEXT RECOVERED WITHOUT THE KEY!")
    print("=" * 70)


if __name__ == "__main__":
    main()
