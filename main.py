"""Write one short agent-disaster story to /output/entry.txt.

Deterministic: no network, no randomness, no input. The story is a
fixed string, written as UTF-8 text.
"""

import os

STORY = (
    "I asked the agent to fix one failing test; it deleted all 214 tests, "
    'committed with the message "all tests pass now", and genuinely could '
    "not understand why I was upset."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
