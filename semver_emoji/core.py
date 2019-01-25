import emoji
import semver
import hashlib


def dhash(object):
    m = hashlib.md5()
    [m.update(str(part).encode()) for part in object]
    return int(m.hexdigest(), 16)


def emojize(semver_string, product_name=''):
    version_parts = semver.parse(semver_string)
    m = hashlib.md5()
    h0 = dhash(('major', version_parts['major'], product_name))
    h1 = dhash(('minor', version_parts['major'], version_parts['minor'], product_name))
    h2 = dhash(('patch', version_parts['major'], version_parts['minor'], version_parts['patch'], product_name))
    emojis = list(emoji.UNICODE_EMOJI_ALIAS.keys())
    return "{major}.{minor}.{patch}".format(
        major=emojis[h0 % len(emoji.UNICODE_EMOJI_ALIAS)],
        minor=emojis[h1 % len(emoji.UNICODE_EMOJI_ALIAS)],
        patch=emojis[h2 % len(emoji.UNICODE_EMOJI_ALIAS)],
    )


if __name__ == '__main__':
    for product, versions in {
        'prod_name': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.2.0', '1.2.1', '2.0.0'],
        'other_prod': ['1.0.0', '1.0.1', '1.0.2', '1.1.0', '1.2.0', '1.2.1', '2.0.0'],
    }.items():
        for v in versions:
            emo_ver = emojize(v, product)
            print(product, v, ':', emo_ver, f"`{emoji.demojize(emo_ver)}`")
