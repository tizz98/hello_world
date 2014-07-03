import hashlib

m = hashlib.md5()

def e():
	if the_world_is_round():
		fun_time = True
		fun = "FUN"

		for letter in fun:
			m.update(letter)
			two_chainz = m.hexdigest()

		if two_chainz:
			return "e"

def the_world_is_round():
	import hashlib

	m = hashlib.md5()
	m.update("e")

	my_letter = m.hexdigest()
	soup = []

	for digit in my_letter:
		m.update(digit)
		soup.append(m.hexdigest())

	if soup:
		return True