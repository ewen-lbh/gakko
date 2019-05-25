from src.core.consts import DURATION_FMT_EXTRACT, DURATION_FMT


def fromstr(string: str):
    if not DURATION_FMT_EXTRACT.match(string):
        return False

    components = [m.groupdict() for m in DURATION_FMT_EXTRACT.finditer(string)][0]
    if not components['h'] and not components['m']:
        return False

    if not components['h']:
        components['h'] = 0

    if not components['m']:
        components['m'] = 0

    if int(components['h']) >= 24:
        return False
    if int(components['m']) >= 60:
        return False

    return components


def tostr(duration_components: dict) -> str:
    return DURATION_FMT.format(**duration_components)


def add(duration1, duration2):
    h = int(duration1['h']) + int(duration2['h'])
    m = int(duration1['m']) + int(duration2['m'])

    while h >= 24 or m >= 60:
        if h >= 24:
            h -= 24
        if m >= 60:
            m -= 60
            h += 1

    return {
        'h': h, 'm': m
    }
