#!/usr/bin/env python3
"""news-image-20261120 entrypoint: copy the front-page image to /output.

The image (entry.png, drawn for Friday 20 November 2026) sits beside
this file in the repository. The program only copies bytes, so two runs
always write the same file. Standard library only, no network.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"

src = os.path.join(HERE, "entry.png")
with open(src, "rb") as fh:
    head = fh.read(8)
assert head == PNG_MAGIC or head[:3] == JPEG_MAGIC, "entry.png is not PNG/JPEG"
size = os.path.getsize(src)
assert size <= MAX_BYTES, f"entry.png is {size} bytes, over the 1 MiB limit"

os.makedirs(OUT_DIR, exist_ok=True)
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(src, dst)
assert os.path.getsize(dst) == size
print(f"wrote {dst} ({size} bytes, sha256 "
      f"{hashlib.sha256(open(dst, 'rb').read()).hexdigest()[:16]})")
