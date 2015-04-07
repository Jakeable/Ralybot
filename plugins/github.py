import re
import requests

from cloudbot import hook
from cloudbot.util import web, formatting

GH_RE = re.compile(r'(.*:)//(www.)?(github.com)(.*)')
API_BASE = 'https://api.github.com/'
API_REPO = API_BASE + "repo/{}"

shortcuts = {
    'cloudbot': 'CloudBotIRC/CloudBot',
    'ae2': 'AppliedEnergistics/Applied-Energistics-2'
}

# Data Fetching
def repo_get_with_search(endpoint, term):
    """
    Searches :endpoint on GitHub for :term and returns an item.
    :param endpoint: API endpoint to search
    :param term: Term to search for.
    :return:
    """
    try:
        params = {'repo/': term}
        request = requests.get(API_REPO.format(endpoint), params=params)
        request.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        raise APIError("Could not find {}: {}".format(endpoint, e))


def get_with_url(url):
    """
    Takes a GitHub URL and returns an item.
    :param url: URL to fetch data on.
    :return:
    """
    try:
        params = {'url': url}
        request = requests.get(API_REPO.format('resolve'), params=params)
        request.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        raise APIError("{}".format(e))

# Data Formatting
def format_repo(repo, show_url=True):
    """
    Takes a GitHub repository and returns a formatted string.
    """
    out = repo['name']

    out += " (\x02{}\x02)".format(repo['owner']['login'])

    out += " \x12|\x12 {} \x12|\x12 {} stars \x12|\x12 {} watchers \x12|\x12 {} forks \x12|\x12 ".format(repo['description'],
                                                                                                         repo['stargazers_count'],
                                                                                                        repo['watchers_count'])

    if show_url:
        out += " - {}".format(web.try_shorten(repo['html_url']))
    return out


@hook.command("ghrepo")
def ghrepo(text):
    """<username> - Retrieves information about the specified GitHub repo."""
    try:
        repo = repo_get_with_search('repo', text)
    except APIError as ae:
        return ae

    if not repo:
        return "No results found."

    try:
        return format_repo(repo)
    except APIError as ae:
        return ae

@hook.command("ghissue", "issue")
def issue(text):
    """<username|repo> [number] - gets issue [number]'s summary, or the open issue count if no issue is specified"""
    args = text.split()
    repo = args[0] if args[0] not in shortcuts else shortcuts[args[0]]
    issue = args[1] if len(args) > 1 else None

    if issue:
        r = requests.get('https://api.github.com/repos/{}/issues/{}'.format(repo, issue))
        j = r.json()

        url = web.try_shorten(j['html_url'], service='git.io')
        number = j['number']
        title = j['title']
        summary = formatting.truncate(j['body'].split('\n')[0], 200)
        if j['state'] == 'open':
            state = '\x033\x02Opened\x02\x0f by {}'.format(j['user']['login'])
        else:
            state = '\x034\x02Closed\x02\x0f by {}'.format(j['closed_by']['login'])

        return '{}: ({}) | {} | {}'.format(title, state, url, summary)
    else:
        r = requests.get('https://api.github.com/repos/{}/issues'.format(repo))
        j = r.json()

        count = len(j)
        if count is 0:
            return 'Repository has no open issues.'.format(count)
        else:
            return 'Repository has {} open issues.'.format(count)

@hook.regex(GH_RE)
def github_url(match):

    url = match.group(1).split(' ')[-1] + "//" + (match.group(2) if match.group(2) else "") + match.group(3) + \
        match.group(4).split(' ')[0]

    item = get_with_url(url)
    if not item:
        return

    if item['kind'] == 'repo':
        return format_repo(repo, show_url=False)

