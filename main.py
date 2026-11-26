"""Worst Monday One-Liners — entry for make.fun.

Writes one funny line about an AI agent's worst Monday to /output/entry.txt.
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
