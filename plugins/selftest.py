from cloudbot import hook

@hook.command(autohelp=False)
def selftest(text):
    """selftest -- Tests the bot's response time."""
    return text + "This is a test to see how fast the bot can respond." + text
