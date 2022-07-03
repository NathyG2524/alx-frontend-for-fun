#!/usr/bin/python3
import sys
import os


if(len(sys.argv) < 3):
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    exit(1)

markdown = sys.argv[1]
file_exits = os.path.exists(markdown)
if not (file_exits):
    sys.stderr.write(f"Missing {markdown}")
    exit(1)
