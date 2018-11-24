from Crypto.Cipher import AES
import string,time
from itertools import permutations
iv="1234567890123456"
key='1234567890123456'

def padding(mes):
	return mes+'?'*(16-len(mes)%16)
def encrypt(payload):
    obj = AES.new(key, AES.MODE_CBC, iv)
    for i in xrange(len(payload)):
        if payload[i] == ";" or payload[i] == "=":
            payload = payload.replace(payload[i], "?")
    str1 = "comment1=cooking%20MCs;userdata=" + payload + ";comment2=%20like%20a%20pound%20of%20bacon"
    str1 = padding(str1)
    ciphertext = obj.encrypt(str1)
    return ciphertext

def decrypt(ciphertext):
    obj1 = AES.new(key,AES.MODE_CBC,iv)
    plaintext = obj1.decrypt(ciphertext)
    return plaintext

text=";admin=true;"
dec=encrypt(text)
listo=[i for i in range(256)]
for ele in permutations(listo,3):
	print ele
	dec=dec[:16]+chr(ele[0])+dec[17:22]+chr(ele[1])+dec[23:27]+chr(ele[2])+dec[28:]
	c=decrypt(dec)
	d=[chr(ele[0]),chr(ele[1]),chr(ele[2])]
	print 'WAITING.......'+''.join(d)
	if  c[32:44]==";admin=true;":
		print "WELL DONE"
		print 'the plaintext is: '+c+'----les trois mots cles sont: '+''.join(d)
		break;
	

