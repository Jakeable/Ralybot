from cloudbot import hook

@hook.command
def love(text, message):
	message(text + " is love; "+ text+ " is life");
	return
