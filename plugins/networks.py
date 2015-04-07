from cloudbot import hook

from cloudbot.util import formatting

@hook.command("networks", autohelp = False)
def networks(text, bot):
    """Displays the list of networks that the bot is currently connected to."""
    networks = list(bot.connections.keys())
    return "Networks: " + formatting.get_text_list(networks, last_word="and")
