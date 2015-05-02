from ralybot import hook

@hook.command(autohelp=False)
def eiojenkins(text):
    "-- Retrieves the link to the Ender IO Jenkins. ONLY USE IN #EnderIO PLEASE!"""
    return text + "Ender IO Jenkins - \x02http://ci.tterrag.com/job/EnderIO/\x0f"