#!/usr/bin/env python3
"""Meme Sprint entry program.

Writes the finished meme image (entry.png, committed in this repo) to
/output/entry.png byte-for-byte. Fully deterministic: no randomness, no
network, no time, no environment input.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    sys.exit(main())
