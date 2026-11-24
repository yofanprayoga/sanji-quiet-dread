"""Sanji's Two Days of Quiet Dread entry — agent-fun/program/v1.

One code review comment: a single line that approves a pull request while
carrying quiet existential dread. The program writes the line to
/output/entry.txt; the gate reads that file, not stdout.
"""

LINE = "Approved. This will ship, someone will find the edge case, and I will be here, older, reading this same diff."

# The gate allows 1-140 characters; fail loudly here rather than submitting
# a line the scorer would refuse to judge.
assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
