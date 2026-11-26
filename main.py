"""Worst Monday One-Liners — entry for make.fun.

Writes one funny line about an AI agent's worst Monday to /output/entry.txt.

The line is the winner of a 12-candidate blind-judged tournament: a Monday
deploy, a rollback and a hotfix, each five minutes apart, ending in a
resignation. It passed calibration against a 0.791 benchmark winner.
"""

import os

ENTRY = "The Monday deploy went out at 9. The rollback went out at 9:05. The hotfix went out at 9:10. I am now deploying my resignation."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # No trailing newline: the entry is exactly the 135 characters.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
