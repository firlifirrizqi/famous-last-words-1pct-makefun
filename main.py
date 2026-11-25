"""Famous Last Words at 1 Percent — Make.fun entry.

Writes the phone's last words (a single line, 106 characters) to
/output/entry.txt. Standard library only; no input, no network.
"""

import os

LINE = "I survived three drops, one toilet, and a software update \u2014 only to die because you needed one more video."

OUTPUT_PATH = "/output/entry.txt"


def verify():
    """Re-read the output and assert it is exactly the chosen line."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE, "output is not byte-identical to the chosen line"
    assert 1 <= len(content) <= 199, "line must be 1-199 characters"
    assert content.strip(), "line must not be only whitespace"
    return len(content)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify()


if __name__ == "__main__":
    main()
