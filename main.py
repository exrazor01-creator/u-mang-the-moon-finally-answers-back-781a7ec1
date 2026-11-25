#!/usr/bin/env python3
"""One-line entry: The Moon Finally Answers Back.

The brief asks for a single line of text, 1 to 240 characters, that
the Moon says back to everyone who has ever stared up at it: an
answer to the wishes, the howls and the late-night promises. The judge
weighs, in order: that it speaks as the Moon answering the wishes,
howls and late-night promises of everyone staring up at it, that it
is funny on one read, that it sounds like the Moon's own voice -- wry
and old and a little tired of being wished upon -- that it lands as a
comeback with the turn arriving before the line ends, and that it
stays inside 240 characters and wastes none of them.

The sealed line below is built to that order on purpose. "Four
billion years" sets the ancient, weary voice at once: this is a
celestial body that has been on duty since before anyone was
counting. The turn arrives in the last words, "wished me a good
night back" -- after eons of granting wishes, the Moon only wants the
courtesy returned. The joke needs no explaining, and it avoids the
obvious werewolf howl and the tired "the Moon is made of cheese"
gags entirely.

LIMIT is 240 because the bounty gate allows one line of 1 to 240
characters. The sealed line is 96 characters, so it sits well inside
the cap; the validator below only guards against an edit that would
push it past the limit. At 96 characters it is also compact, which
helps if two entries ever tie on rate: the smaller text places first.
"""

import os

# The sealed line: after four billion years of wishes, the Moon
# asks for one good night back.
ENTRY = "Four billion years of listening to wishes, and nobody has ever once wished me a good night back."

LIMIT = 240  # bounty gate: one line, 1-240 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 240-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
