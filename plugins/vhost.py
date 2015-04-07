import asyncio

from cloudbot import hook

@asyncio.coroutine
@hook.irc_raw('004')
def onready(conn):
    conn.message("BotServ", "ON")
