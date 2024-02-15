#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # If all conditions are met, print nothing and exit 0
    sys.exit(0)
