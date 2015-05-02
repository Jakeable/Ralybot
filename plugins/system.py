import os
import time
import platform
from datetime import timedelta

import psutil

from ralybot import hook
from ralybot.util.filesize import size as format_bytes
import ralybot


@hook.command(autohelp=False)
def about(text, conn):
    """-- Gives information about Ralybot. Use 'about license for information about the license and 'about source to get the source code for the bot."""
    if text.lower() in ("license", "gpl"):
        return "Ralybot is released under the GPL v3 license."
    
    if text.lower() in ("src", "source"):
        return "Ralybot is open source! Get the source code at https://github.com/KamranMackey/Ralybot."

    return "{} is a simple, fast, extendable, and open source IRC bot coded in Python. ({})".format(conn.nick, ralybot.__version__)


@hook.command(autohelp=False)
def system():
    """-- Retrieves information about the system running the bot."""
    process = psutil.Process(os.getpid())

    # get the data we need using the Process we got
    cpu_usage = process.get_cpu_percent()
    thread_count = process.get_num_threads()
    memory_usage = format_bytes(process.get_memory_info()[0])

    # Get general system info
    sys_os = platform.platform()
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    sys_architecture = '-'.join(platform.architecture())
    sys_cpu_count = platform.machine()

    # Get uptime
    uptime = timedelta(seconds=round(time.time() - process.create_time()))

    return (
        "Operating System: \x02{}\x02, "
        "Python: \x02{} {}\x02, "
        "Architecture: \x02{}\x02 (\x02{}\x02)\n"
        "Uptime: \x02{}\x02, "
        "Threads: \x02{}\x02, "
        "CPU Usage: \x02{}\x02, "
        "Memory Usage: \x02{}\x02"
    ).format(
        sys_os,
        python_implementation,
        python_version,
        sys_architecture,
        sys_cpu_count,
        uptime,
        thread_count,
        cpu_usage,
        memory_usage,
    )
