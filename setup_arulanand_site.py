#!/usr/bin/env python3
"""setup_arulanand_site.py — regenerates the site files locally."""
import os, sys, subprocess
TARGET = r"C:\\Git\\arulanand.github.io"
FILES = {}
def write_files():
    for rel,content in FILES.items():
        dest=os.path.join(TARGET,*rel.split("/"))
        os.makedirs(os.path.dirname(dest),exist_ok=True)
        open(dest,"w",encoding="utf-8",newline="\n").write(content)
        print("  wrote",rel)
if __name__=="__main__":
    print("Writing files under",TARGET)
    os.makedirs(TARGET,exist_ok=True); write_files()
    print("Done. Then: git add . && git commit -m \"Update site\" && git push")
