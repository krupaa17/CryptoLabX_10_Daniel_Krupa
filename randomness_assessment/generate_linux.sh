#!/usr/bin/env bash
set -euo pipefail

bytes="${1:-1048576}"
output_dir="${2:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/generated}"

if ! [[ "$bytes" =~ ^[0-9]+$ ]] || (( bytes < 1048576 )); then
    echo "Size must be an integer of at least 1048576 bytes." >&2
    exit 2
fi

mkdir -p "$output_dir"
head -c "$bytes" /dev/urandom > "$output_dir/linux_urandom.bin"
openssl rand -out "$output_dir/openssl_rand.bin" "$bytes"

for file in "$output_dir/linux_urandom.bin" "$output_dir/openssl_rand.bin"; do
    actual_size="$(wc -c < "$file")"
    if (( actual_size != bytes )); then
        echo "Expected $bytes bytes in $file, got $actual_size." >&2
        exit 1
    fi
    printf '%s: %s bytes\n' "$file" "$actual_size"
done
