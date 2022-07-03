#!/usr/bin/python3
import sys
import os
import markdown

if(len(sys.argv) < 2):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

markdowni = sys.argv[1]
file_exits = os.path.exists(markdowni)
if not (file_exits):
    print(f"Missing {markdowni}")
    exit(1)


markdown.markdownFromFile(
    input="README.md",
    output="README.html",
    encoding='utf8',
)
