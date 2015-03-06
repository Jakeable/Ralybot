import cloudbot
from cloudbot import hook

@hook.command("ver", "version", autohelp=False)
def version(text, conn):
    """-- Displays the bot's version number."""
    return "{} is currently running bot version {}." .format(conn.nick, cloudbot.__version__)
