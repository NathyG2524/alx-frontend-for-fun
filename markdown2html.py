#!/usr/bin/python3
import sys
import os
# import markdown

if(len(sys.argv) < 2):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

markdowni = sys.argv[1]
htmlfile = sys.argv[2]
file_exits = os.path.exists(markdowni)
if not (file_exits):
    print(f"Missing {markdowni}")
    exit(1)


with open(markdowni, 'r') as mark:
    lis = []
    num = []
    for line in mark.readlines():
        result = line.split()
        # for sym in result[0]:
        #     fresult = sym.split(" ")
        # print(len(result[0]))
        # print(result[1])
        # print(result[2])

        lis.append(f"<h{len(result[0])}>{result[1]} {result[2]}</h{len(result[0])}>\n")
        num.append(len(result[0]))
    



with open(htmlfile, 'w',  encoding="utf-8") as html:
    html.writelines(lis)
