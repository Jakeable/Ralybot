import codecs
import json
import os
import random
import asyncio
import re

from ralybot import hook
from ralybot.util import textgen
from ralybot.event import EventType

nick_re = re.compile("^[A-Za-z0-9_|.\-\]\[\{\}]*$", re.I)


def is_valid(target):
    """ Checks if a string is a valid IRC nick. """
    if nick_re.match(target):
        return True
    else:
        return False


def is_self(conn, target):
    """ Checks if a string is "****self" or contains conn.name. """
    if re.search("(^..?.?.?self|{})".format(re.escape(conn.nick)), target, re.I):
        return True
    else:
        return False


@hook.on_start()
def load_attacks(bot):
    """
    :type bot: ralybot.bot.Ralybot
    """
    global larts, flirts, kills, slaps, insults, wreck

    with codecs.open(os.path.join(bot.data_dir, "larts.txt"), encoding="utf-8") as f:
        larts = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "flirts.txt"), encoding="utf-8") as f:
        flirts = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "insults.txt"), encoding="utf-8") as f:
        insults = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "kills.json"), encoding="utf-8") as f:
        kills = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "slaps.json"), encoding="utf-8") as f:
        slaps = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "wreck.json"), encoding="utf-8") as f:
        wreck = json.load(f)


@asyncio.coroutine
@hook.command
def lart(text, conn, nick, action):
    """<user> - LARTs <user>"""
    target = text.strip()

    if not is_valid(target):
        return "I can't attack that, since it's not a valid target. " \
         "Please choose a valid target for me to lart!"

    if is_self(conn, target):
        # When the user is trying to make the bot attack itself, make the
        # bot attack the user who is doing the command.
        target = nick

    phrase = random.choice(larts)

    # act out the message
    action(phrase.format(user=target))


@asyncio.coroutine
@hook.command
def flirt(text, conn, nick, message):
    """<user> - flirts with <user>"""
    target = text.strip()

    if not is_valid(target):
        return "I can't flirt with that, since it's not a valid target. " \
         "Please choose a valid target for me to flirt with!"

    if is_self(conn, target):
        # When the user is trying to make the bot attack itself, make the
        # bot attack the user who is doing the command.
        target = nick

    message('{}, {}'.format(target, random.choice(flirts)))


@asyncio.coroutine
@hook.command
def kill(text, conn, nick, action):
    """<user> - kills <user>"""
    target = text.strip()

    if not is_valid(target):
        return "I can't attack that, since it's not a valid target. " \
         "Please choose a valid target for me to kill!"

    if is_self(conn, target):
        # When the user is trying to make the bot attack itself, make the
        # bot attack the user who is doing the command.
        target = nick

    generator = textgen.TextGenerator(kills["templates"], kills["parts"], variables={"user": target})

    # act out the message
    action(generator.generate_string())


@asyncio.coroutine
@hook.command
def slap(text, action, nick, conn, notice):
    """<user> -- Makes the bot slap <user>."""
    target = text.strip()

    if not is_valid(target):
        return "I can't slap that, since it's not a valid target. " \
         "Please choose a valid target for me to slap!"

    if is_self(conn, target):
        # When the user is trying to make the bot attack itself, make the
        # bot attack the user who is doing the command.
        target = nick

    variables = {
        "user": target
    }
    generator = textgen.TextGenerator(slaps["templates"], slaps["parts"], variables=variables)

    # Act out the message.
    action(generator.generate_string())

@asyncio.coroutine
@hook.command
def wreck(text, conn, nick, action):
    """<user> - Makes the bot wreck <user>."""
    target = text.strip()

    if not is_valid(target):
         return "I can't wreck that, since it's not a valid target. " \
         "Please choose a valid target for me to wreck!"

    if is_self(conn, target):
        # When the user is trying to make the bot attack itself, make the
        # bot attack the user who is doing the command.
        target = nick

    generator = textgen.TextGenerator(wreck["templates"], wreck["parts"], variables={"user": target})

    # Act out the message.
    action(generator.generate_string())

@asyncio.coroutine
@hook.command()
def insult(text, conn, nick, notice, message):
    """<user> - insults <user>
    :type text: str
    :type conn: ralybot.client.Client
    :type nick: str
    """
    target = text.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # When the user is trying to make the bot attack itself, make the
    # bot attack the user who is doing the command.
    if is_self(conn, target):
        target = nick

    message("{}, {}".format(target, random.choice(insults)))

@hook.command
def punch(text, action):
    """<user> - punches <user>"""
    text = text.strip()

    if text.lower() == "kamran":
        return "No."

    action('punches {}.'.format(text))
    action('punches {} again.'.format(text))
    action('punches {} a few more times.'.format(text))
    action('punches {} one last time for good measure.'.format(text))