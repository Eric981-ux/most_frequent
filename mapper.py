#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t')
        print(f"MAX\t{word} {count}")
    except ValueError:
        continue  # skip malformed lines
