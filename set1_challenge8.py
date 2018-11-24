import base64
from Crypto.Cipher import AES

ciphertexts = [line.strip().decode('hex') for line in open("file1.txt")]
mes=ciphertexts[132]
key="YELLOW SUBMARINE"

crypter = AES.new(key, AES.MODE_ECB)
plaintext = crypter.decrypt(mes)
print plaintext