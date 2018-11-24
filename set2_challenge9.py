

def padding(message,taille_block):
	return message+'?'*(taille_block-len(message)%taille_block)


print padding("YELLOW SUBMARINE",20)