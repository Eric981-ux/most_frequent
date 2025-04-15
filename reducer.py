#!/usr/bin/env python3
import sys

max_word = None
max_count = 0

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        word, count = value.rsplit(' ', 1)
        count = int(count)

        if count > max_count:
            max_count = count
            max_word = word
    except ValueError:
        continue

if max_word:
    print(f"{max_word}\t{max_count}")
