# Assignment 9: Operating-System Randomness

This lab generates at least 1 MiB from Linux `/dev/urandom`, OpenSSL's `rand`
command, and the Windows .NET cryptographic random-number API. The notebook
compares byte frequencies, bit frequencies, bit runs, repeated byte runs,
repeated 16-byte blocks, and byte correlations at lags 1, 2, 4, and 16. It uses
a byte-frequency chi-square test and the monobit and runs tests on the bit
stream.

## Generate the samples

Run the Linux capture script on Linux (or inside WSL) from the repository root:

```bash
bash randomness_assessment/generate_linux.sh
```

It creates `randomness_assessment/generated/linux_urandom.bin` and
`randomness_assessment/generated/openssl_rand.bin`.

Run the Windows capture script in PowerShell from the repository root:

```powershell
.\randomness_assessment\generate_windows.ps1
```

If PowerShell blocks the script due to the current process execution policy, use
a one-time process-scoped policy for this command:

```powershell
powershell -ExecutionPolicy Bypass -File .\randomness_assessment\generate_windows.ps1
```

It creates `randomness_assessment/generated/windows_dotnet_rng.bin`. Both scripts
accept an optional byte count but refuse sizes below 1 MiB. Generated binary
samples are intentionally ignored by Git; regenerate them on the operating
systems being compared.

## Analyze in the notebook

Open `randomness_assessment/randomness_analysis.ipynb` in Jupyter or VS Code and
run all cells after generating all three samples. The notebook requires only
Python's standard library. It checks each sample is at least 1 MiB and reports
the test statistics and an interpretation for each.

## Interpreting the results

The chi-square test compares the 256 byte counts to a uniform distribution
(255 degrees of freedom; the 5% critical value is approximately 293.25). The
monobit and runs tests report approximate p-values; small p-values flag
unexpected behavior but do not prove a generator is insecure. Correlation and
duplicate-pattern measurements are descriptive checks. A p-value above a
threshold means only that the test did not detect a deviation in this sample.

Linux maintains a kernel cryptographic random-number generator seeded from
available environmental noise; `/dev/urandom` reads from that generator and
does not expose raw timing events as application bytes. OpenSSL's `rand`
command obtains bytes through OpenSSL's cryptographic random-number generator,
which seeds and reseeds from operating-system entropy sources and maintains
its own DRBG state. On Windows, .NET's `RandomNumberGenerator` uses the
platform cryptographic provider (the implementation depends on the .NET
version). Windows CNG exposes system cryptographic randomness through its
BCrypt interfaces and manages the underlying cryptographic provider state.

Passing statistical tests is not a security proof. Tests observe distributions
and limited dependencies in sampled output; they cannot establish
unpredictability, protect against state compromise, detect every implementation
or integration flaw, or predict future output. Cryptographic suitability also
depends on correct seeding, reseeding, isolation, API use, and the threat model.

## References

- Linux `random(7)`: <https://man7.org/linux/man-pages/man7/random.7.html>
- OpenSSL `RAND_bytes` and `RAND_priv_bytes` documentation:
  <https://docs.openssl.org/3.5/man3/RAND_bytes/>
- .NET `RandomNumberGenerator` API:
  <https://learn.microsoft.com/dotnet/api/system.security.cryptography.randomnumbergenerator>
- Windows CNG overview:
  <https://learn.microsoft.com/windows/win32/seccng/cng-portal>
- NIST SP 800-22 Rev. 1a, Statistical Test Suite:
  <https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final>
