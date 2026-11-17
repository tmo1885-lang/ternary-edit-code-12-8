#!/usr/bin/env python3
"""Standalone certificate verifier for the 12-word ternary edit code."""
from itertools import combinations
from collections import Counter
from pathlib import Path
from hashlib import sha256

GENERATORS = ("000002222211", "000111111222", "002120201010", "022222002222")
EXPECTED_HASH = "7cec0c303acdc6cbc1bf7018ad9af0ab96f89e9d4c37e18c5b4d54887c42b102"

def shift(word, k):
    return "".join(str((int(c) + k) % 3) for c in word)

def distance(a, b):
    previous = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        current = [i] + [0] * len(b)
        for j, y in enumerate(b, 1):
            current[j] = min(previous[j] + 1, current[j-1] + 1,
                             previous[j-1] + (x != y))
        previous = current
    return previous[-1]

def main():
    words = sorted({shift(g, k) for g in GENERATORS for k in range(3)})
    assert len(words) == 12
    certificate = Path(__file__).with_name("codewords.txt").read_bytes()
    assert sha256(certificate).hexdigest() == EXPECTED_HASH
    assert certificate == ("\n".join(words) + "\n").encode("ascii")
    assert all(len(w) == 12 and set(w) <= set("012") for w in words)
    histogram = Counter(distance(a, b) for a, b in combinations(words, 2))
    assert histogram == {8: 57, 9: 3, 10: 3, 11: 3}, histogram
    print("PASS: 12 distinct ternary words of length 12")
    print("Pairwise distance histogram:", dict(sorted(histogram.items())))
    print("Minimum edit distance:", min(histogram))

if __name__ == "__main__":
    main()
