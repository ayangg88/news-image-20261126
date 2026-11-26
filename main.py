"""news-image-20261126 entry: copy the newspaper front page to the output dir.

Python 3.13, standard library only, no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        magic = f.read(8)
    if magic != PNG_MAGIC:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    size = os.path.getsize(dst)
    if size != src_size:
        print(f"copy incomplete: wrote {size} bytes, expected {src_size}",
              file=sys.stderr)
        return 1
    if size > 1048576:
        print(f"entry.png too large: {size} bytes", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
