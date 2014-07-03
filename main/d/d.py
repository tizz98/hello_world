def d():
	# Exclamation points are cool!!!!!!!!!!!!!!
	# I really want to make this last one as
	# complicated as possible because it's the
	# last one, but I'm not quite sure what to do
	# ...again. Here's goes zero effort whatsoever

	import datetime.datetime
	import hashlib

	m = hashlib.md5()
	dt_str = "datetime"
	m.update(dt_str)

	if datetime.today() == datetime.today():
		# everybody say 'yay!'
		if "d" in dt_str:
			# everybody say 'yay!' again
			m.update(m.hexdigest())
			
			return "d"