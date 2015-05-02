import ralybot
from ralybot import hook

@hook.command("ver", "version", autohelp=False)
def version(text, conn):
    """-- Displays Ralybot's current version number."""
    return "{} is currently at version {}." .format(conn.nick, ralybot.__version__)
