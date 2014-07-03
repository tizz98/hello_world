import hashlib

m = hashlib.md5()

def h():
	m.update('hello world')
	hello_world = m.hexdigest()
	my_list = []
	alphabet = True

	for char in hello_world:
		my_list.append(char)

	while ((1 < 2) and alphabet):
		alphabet = False

	if "h" == "h":
		return "h"