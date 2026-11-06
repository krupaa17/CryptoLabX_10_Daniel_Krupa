
import time
from pathlib import Path

from .mt19937_stream_cipher import generate_keystream


timestamp = int(time.time())

token = bytes(generate_keystream(timestamp, 16))

print("========== TOKEN GENERATION ==========")
print("Timestamp:", timestamp)
print("Token:", token.hex())
print("Token length:", len(token), "bytes")


output_file = Path(__file__).with_name("token_record.txt")

with open(output_file, "w") as file:
    file.write(f"Timestamp: {timestamp}\n")
    file.write(f"Token: {token.hex()}\n")


observed_token = token

start_time = timestamp - 300
end_time = timestamp + 300

print("\n========== TOKEN PREDICTION ATTACK ==========")
print("Search interval:", start_time, "to", end_time)

recovered_timestamp = None
candidates_tested = 0

for candidate_time in range(start_time, end_time + 1):
    candidate_token = bytes(
        generate_keystream(candidate_time, 16)
    )

    candidates_tested += 1

    if candidate_token == observed_token:
        recovered_timestamp = candidate_time
        break


print("\n========== ATTACK RESULTS ==========")
print("Candidates tested:", candidates_tested)
print("Recovered timestamp:", recovered_timestamp)


if recovered_timestamp is not None:
    verified_token = bytes(
        generate_keystream(recovered_timestamp, 16)
    )

    print("\n========== VERIFICATION ==========")
    print("Original token:", observed_token.hex())
    print("Regenerated token:", verified_token.hex())
    print("Timestamp recovered:",
          recovered_timestamp == timestamp)
    print("Token verification:",
          verified_token == observed_token)
else:
    print("No matching timestamp found.")
