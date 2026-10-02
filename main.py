"""PDF Watermark — Stamp a text watermark on every page of a PDF and write a new file."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pdf_watermark',
        description='Stamp a text watermark on every page of a PDF and write a new file.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PDF Watermark')
    print('DRAFT or CONFIDENTIAL on local PDFs.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
