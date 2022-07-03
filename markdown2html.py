#!/usr/bin/python3
import sys
import os

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)

    markdown = sys.argv[1]
    file_exits = os.path.exists(markdown)
    if not (file_exits):
        print(f"Missing {markdown}", file=sys.stderr)
