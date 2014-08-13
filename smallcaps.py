#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pandoc filter to convert all regular text to uppercase.
Code, link URLs, etc. are not affected.
"""
from pandocfilters import *

Str2 = elt('Str2', 1)

def small_caps(key, value, format, meta):
    min_length = 4
    if key != 'Str' or len(value) <= min_length:
        return None

    if value[:min_length].isupper():
        # So we have 's or ’s (fancy apostrophe)
        if value[-2:] in [u"'s", u"’s"]:
            return [SmallCaps([Str2(value[:-2])]),
                    Str2(value[-2:])]
        # A pluralized acronym
        elif value[-1] == 's':
            return [SmallCaps([Str2(value[:-1])]),
                    Str2(value[-1])]
        else:
            return SmallCaps([Str2(value)])

def replace_str2(key, value, format, meta):
    if key == 'Str2':
        return Str(value)

def toJSONFilter_pure(doc, actions, format):
    altered = doc
    for action in actions:
        altered = walk(altered, action, format, doc[0]['unMeta'])
    return altered

if __name__ == "__main__":
    doc = json.loads(sys.stdin.read())
    if len(sys.argv) > 1:
        format = sys.argv[1]
    else:
        format = ""
    altered = toJSONFilter_pure(doc, [small_caps, replace_str2], format)
    json.dump(altered, sys.stdout)
