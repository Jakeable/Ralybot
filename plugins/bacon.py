from ralybot import hook

@hook.command(autohelp=False)
def bacon(text):
    "-- BACON!"""
    return text + "BACON BACON BACON!!!"