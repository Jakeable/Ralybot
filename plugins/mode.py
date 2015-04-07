import asyncio

from cloudbot import hook

@asyncio.coroutine
@hook.irc_raw('004')
def onready(conn):
    conn.send("MODE {} +B".format(conn.nick))
