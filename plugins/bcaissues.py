from cloudbot import hook

@hook.command(autohelp=False)
def bcaissues(text):
    "-- Retrieves the link to the BuildCraft Additions Issue Tracker on GitHub. ONLY USE IN #buildcraftAdditions PLEASE!"""
    return text + "BuildCraft Additions Issue Tracker - \x02https://github.com/BCA-Team/BuildCraft-Additions/issues\x0f"
