def o():
	hell = Bloody()
	the_meaning = hell.meaning()

	for x in xrange(1,666):
		death = hell.death()

	life = death
	fun = life

	my_name_is_paul = True

	return "oi"[0]


class Hell(object):
	satan = "dude"
	evil_minions = True
	num_em = 666

	def death(self):
		self.num_em = self.num_em + 1
		return "you dead, son"


class Bloody(Hell):

	def meaning(self):
		return "lovely british saying, you bloody bloke"