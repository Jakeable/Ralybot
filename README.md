# Ralybot

Ralybot is a simple, fast, expandable open-source Python IRC bot, and is a fork of another awesome bot called CloudBot.

## Getting Ralybot

There are currently two different branches of this repository, each with a different level of stability:
 - **python3.4** *(main, but unstable!)*: This branch is the main branch in the repository, but might contain unstable, untested code. You have been warned!

## Installing Ralybot

Firstly, Ralybot will only run on **Python 3.4 or higher**. Because we use the asyncio module, you will not be able to use any other versions of Python.

To install Ralybot on *nix (linux, etc), see [here](https://github.com/CloudBotIRC/CloudBot/wiki/Installing-on-*nix)

To install Ralybot on Windows, see [here](https://github.com/CloudBotIRC/CloudBot/wiki/Installing-on-Windows)


### Running Ralybot

Before you run the bot, rename `config.default.json` to `config.json` and edit it with your preferred settings. You can check if your JSON is valid using [jsonlint.com](http://jsonlint.com/)!

Once you have installed the required dependencies and renamed the config file, you can run the bot! Make sure you are in the correct folder and run the following command:

```
python3.4 -m Ralybot
```

Note that you can also run the `cloudbot/__main__.py` file directly, which will work from any directory.
```
python3.4 Ralybot/cloudbot/__main__.py
```
Specify the path as /path/to/repository/cloudbot/__main__.py, where `cloudbot` is inside the repository directory.

## Getting help with Ralybot

### Documentation

The Ralybot documentation is currently somewhat outdated and may not be correct. If you need any help, please visit our [IRC channel](irc://irc.esper.net/cloudbot) and we will be happy to assist you.

To write your own plugins, visit the [Plugins Wiki Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki/Writing-Refresh-Modules).

More at the [Wiki Main Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki).

### Support

The developers reside in [#Ralybott](irc://irc.esper.net/Ralybot) on the [EsperNet](http://esper.net) IRC network, and would be glad to help you.

If you think you have found a bug/have a idea/suggestion, please **open a issue** here on Github and contact us on IRC!

## Example Ralybots

You can find a number of example bots in [#Ralybot](irc://irc.esper.net/Ralybot "Connect via IRC to #Ralybot on irc.esper.net").

## Changelog

See [CHANGELOG.md](https://github.com/KamranMackey/Ralybot/blob/master/CHANGELOG.md)
