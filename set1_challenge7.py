import base64
from Crypto.Cipher import AES

mes="CRIwqt4+szDbqkNY+I0qbDe3LQz0wiw0SuxBQtAM5TDdMbjCMD/venUDW9BL"
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
key="YELLOW SUBMARINE"
ciphertext = base64.b64decode(mes)
crypter = AES.new(key, AES.MODE_ECB)
plaintext = crypter.decrypt(ciphertext[:32])

print plaintext

f=open('file')
while(f.readline()):
 	mes=f.readline()
 	ciphertext = base64.b64decode(mes)
 	crypter = AES.new(key, AES.MODE_ECB)
 	plaintext = unpad(crypter.decrypt(ciphertext[:32]))
	print plaintext

#I'm back and I'm ringin' the bel