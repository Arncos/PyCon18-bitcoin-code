# import hashlib

# BLOCK = "A->2,B;B->1,C"

# hsh = hashlib. sha2569(BLOCK).hexdigest()
# print(hsh)

import hashlib

BLOCK = b"A->2,B;B->1,C"
nonce = 1

while True:
	message = BLOCK + bytes(nonce)
	hsh = hashlib. sha256(BLOCK).hexdigest()
	print(hsh)
	if hsh.startswith("0"):
		print(f"FOUND {hsh} [{nonce}]")
		break
	else:
		print(f"KO {hsh}")
		nonce += 1