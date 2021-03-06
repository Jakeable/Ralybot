# Ralybot 
[![Documentation Status](https://readthedocs.org/projects/ralybot/badge/?version=latest)](https://readthedocs.org/projects/ralybot/?badge=latest) 
[![Build Status](https://travis-ci.org/KamranMackey/Ralybot.svg?branch=python3.4)](https://travis-ci.org/KamranMackey/Ralybot) 
[![Requirements Status](https://requires.io/github/KamranMackey/Ralybot/requirements.svg?branch=master)](https://requires.io/github/KamranMackey/Ralybot/requirements/?branch=master)

Ralybot is a simple, fast, expandable and open-source Python IRC bot. Its documentation is on [Read The Docs](https://ralybot.readthedocs.org/en/latest/). I'd also like to mention that Ralybot now has its own Trello board set up. You can find the board [here](https://trello.com/b/olPXxniK/ralybot).

**Note**: The documentation is still a work-in-progress and is not finished yet. You can find the source code for the documentation at the [Ralybot-Docs](https://github.com/KamranMackey/Ralybot-Docs) GitHub repository.

## Getting Ralybot

There are currently two different branches of this repository, each with a different level of stability:
 - **master** *(main, but unstable!)*: This branch is the main branch in the repository, but might contain unstable, untested code. You have been warned!

## Installing Ralybot

Firstly, Ralybot will only run on **Python 3.4 or higher**. Because we use the asyncio module, you will not be able to use any other versions of Python.

To install Ralybot on *nix (Linux, etc), see [here](https://github.com/CloudBotIRC/CloudBot/wiki/Installing-on-*nix).

To install Ralybot on Windows, see [here](https://github.com/CloudBotIRC/CloudBot/wiki/Installing-on-Windows).


### Running Ralybot

Before you run the bot, make sure you rename `config.default.json` to `config.json` and edit it with your preferred settings. You can check if your JSON is valid using [jsonlint.com](http://jsonlint.com/)!

Once you have installed the required dependencies and renamed the config file, you can run the bot! Make sure you are in the correct folder and run the following command in a terminal:

```
python3.4 -m ralybot
```

Note that you can also run the `ralybot/__main__.py` file directly, which will work from any directory.
```
python3.4 Ralybot/ralybot/__main__.py
```
Specify the path as /path/to/repository/ralybot/__main__.py, where `ralybot` is inside the repository directory.

## Getting help with Ralybot

### New Issue Tracker & Wiki
Ralybot will soon be moving to a different issue tracker called [JIRA](https://www.atlassian.com/software/jira) and a different wiki platform called [Confluence](https://www.atlassian.com/software/confluence) which are both developed by [Atlassian](https://www.atlassian.com). I will be hosting the instances myself on my own server. This means that the issue tracker and wiki that we are using currently (The GitHub issue tracker and wiki) will be disabled once I get the JIRA & Confluence instances all setup and configured. 

### Documentation

The Ralybot documentation is currently somewhat outdated and may not be correct. If you need any help, please visit our [IRC channel](irc://irc.esper.net/ralybot) and we will be happy to assist you.

To write your own plugins, visit the [Plugins Wiki Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki/Writing-Refresh-Modules).

More information is at the [Wiki Main Page](https://github.com/CloudBotIRC/CloudBotRefresh/wiki).

### Support

The developers reside in [#Ralybot](irc://irc.esper.net/Ralybot) on the [EsperNet](http://esper.net) IRC network, and would be glad to help you.

If you think you have found a bug/have a idea/suggestion, please **open a issue** here on GitHub and contact us on IRC!

## Changelog

See [CHANGELOG.md](https://github.com/KamranMackey/Ralybot/blob/master/CHANGELOG.md) for the changelog. **WARNING!**: The changelog is not always updated and may be out of date with the current release version. You have been warned.

## License

Ralybot is **licensed** under the **GPL v3** license. The terms are as follows.

![GPL V3](https://www.gnu.org/graphics/gplv3-127x51.png)

    Ralybot

    Copyright © 2015 Kamran Mackey / Ralybot Project
    Copyright © 2011-2015 Luke Rogers / CloudBot Project

    Ralybot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Ralybot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Ralybot. If not, see <http://www.gnu.org/licenses/>.

This product includes GeoLite2 data created by MaxMind, available from
<a href="http://www.maxmind.com">http://www.maxmind.com</a>. GeoLite2 databases are distributed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/)

This product uses data from <a href="http://wordnik.com">http://wordnik.com</a> in accordance with the wordnik.com API <a href="http://developer.wordnik.com/#!/terms">Terms of Service</a>.
