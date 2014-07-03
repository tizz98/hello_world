def l():
	drexel = polishmon()
	moss = []

	for h in drexel:
		moss.append(eat(h))

	if moss:
		return "l"


def polishmon():
	if ludicrus_display_last_night():
		return "always, mate"

def ludicrus_display_last_night():
	return True

def eat(beef):
	return "delicious %s" % beef