#!/usr/bin/env python3
import re
import sys

class Color:
    WARNING = '\033[93m'
    FAIL = '\033[91m'

if __name__ == "__main__":
    regex = r'^(feat|fix|docs|style|refactor|perf|test|chore)(\s(feat|fix|docs|style|refactor|perf|test|chore))*\([^\)]+\):\s.+$'
    commit_message_file = sys.argv[1]
    message = open(commit_message_file).read().strip()

    if not re.match(regex, message):
        print(f"{Color.FAIL}Error: Not a valid commit message!")
        print("Read git guidelines at: https://wiki.nickelfox.com/books/web-frontend-development/page/github-guidelines")
        sys.exit(1)
