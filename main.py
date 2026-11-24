"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one funny single-line one-star review from a house
# cat about its human: 154 characters, one line, inside the 200-char
# gate. Specific complaints (food bowl, laptop keyboard, coffee),
# deadpan review shape, and the sting lands in the last two words.
# Revision note: re-read the gate after running; 154 characters,
# one line, no trailing newline.
import os

TEXT = (
    "One star. He fills my bowl, then types on MY laptop for hours. "
    "I knocked his coffee off the table to restore balance. He called "
    "it an accident. It wasn't."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
