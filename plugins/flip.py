replacements = {
    'a': '?',
    'b': 'q',
    'c': '?',
    'd': 'p',
    'e': '?',
    'f': '?',
    'g': '?',
    'h': '?',
    'i': '?',
    'j': '?',
    'k': '?',
    'l': '?',
    'm': '?',
    'n': 'u',
    'o': 'o',
    'p': 'd',
    'q': 'b',
    'r': '?',
    's': 's',
    't': '?',
    'u': 'n',
    'v': '?',
    'w': '?',
    'x': 'x',
    'y': '?',
    'z': 'z',
    '?': '¿',
    '.': '?',
    ',': '\'',
    '(': ')',
    '<': '>',
    '[': ']',
    '{': '}',
    '\'': ',',
    '_': '?'}

# append an inverted form of replacements to itself, so flipping works both ways
replacements.update(dict((v, k) for k, v in replacements.items()))

flippers = ["( ????)?", "(?°?°)?", "( ???? )?"]


@hook.command
def flip(text, reply):
    """<text> -- Flips <text> over."""
    reply(formatting.multi_replace(text[::-1].lower(), replacements))


@hook.command(autohelp=False)
def table(text, message):
    """<text> -- (?°?°)?? <?x??>"""
    if text:
        message(random.choice(flippers) + " ? " + formatting.multi_replace(text[::-1].lower(), replacements))
    else:
        message(random.choice(flippers) + " ? ???")