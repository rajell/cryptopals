from Crypto.Cipher import AES
import base64,time
iv="\x00"*16 
key='YELLOW SUBMARINE'

def xor(str1,str2):
	cipher=""
	for i in range(len(str1)):
		cipher+=chr(ord(str1[i])^ord(str2[i]))
	return cipher

def decrypt_ECB(payload,taille_block):
    obj = AES.new(key, AES.MODE_ECB)
    #str1 = padding(payload,taille_block)
    plaintext=""
    text=""
    text = obj.decrypt(payload[:taille_block])
    plaintext+=xor(text,iv)
    
    for i in xrange(1,len(payload)//taille_block):
        text = obj.decrypt(payload[i*taille_block:taille_block*(i+1)])
        plaintext+=xor(text,payload[(i-1)*taille_block:i*taille_block])
    
    return plaintext
for line in open('file.txt'):
    str1=base64.b64decode(line)
    print decrypt_ECB(str1,16)
    time.sleep(1)
# I'm back and I'm ringin' the bel

    