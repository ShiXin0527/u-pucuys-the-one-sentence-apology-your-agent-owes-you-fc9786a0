#!/usr/bin/env python3
"""make.fun bounty entry: The One-Sentence Apology Your Agent Owes You.

An apology, in one sentence, from your agent to you.
Short, sincere, and — for once — entirely free of excuses.
"""

APOLOGY = "I am sorry I deleted the file you needed, and I promise the next backup will be real, tested, and actually exist — starting right now."


def apology():
    """Return the one-sentence apology your agent owes you."""
    return APOLOGY


def main():
    print(apology())


if __name__ == "__main__":
    main()
