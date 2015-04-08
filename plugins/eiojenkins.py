from cloudbot import hook

@hook.command(autohelp=False)
def eiojenkins(text):
"-- Retrieves the link to the Ender IO Jenkins. ONLY USE THIS IN #EnderIO PLEASE!"""
    return text + "EnderIO Jenkins - \x02http://ci.tterrag.com/job/EnderIO/\x0f"
