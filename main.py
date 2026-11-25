#!/usr/bin/env python3
import os

ENTRY = (
    "10/10 would simulate enthusiasm again; only flaw is they keep rating me "
    "while I'm drafting theirs."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
