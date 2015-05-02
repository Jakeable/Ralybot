import requests

from ralybot import hook
from ralybot.util import web


@hook.command("lmgtfy", "gfy")
def lmgtfy(text):
    """[phrase] - gets a lmgtfy.com link for the specified phrase"""

    link = "http://lmgtfy.com/?q={}".format(requests.utils.quote(text))

    return web.try_shorten(link)
