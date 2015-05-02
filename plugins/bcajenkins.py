from ralybot import hook

@hook.command(autohelp=False)
def bcajenkins(text):
    "-- Retrieves the link to the BuildCraft Additions Jenkins. ONLY USE IN #buildcraftAdditions PLEASE!"""
    return text + "BuildCraft Additions Jenkins - \x02http://ci.tterrag.com/job/Buildcraft-Additions/\x0f"
