"""Render an original Arche Nova PDF page or normalized crop."""
import argparse
from pathlib import Path
import fitz


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', choices=['regelbuch', 'quickstart'])
    parser.add_argument('page', type=int, help='1-based PDF page')
    parser.add_argument('--crop', type=float, nargs=4, metavar=('X0', 'Y0', 'X1', 'Y1'))
    parser.add_argument('--dpi', type=int, default=160)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not 72 <= args.dpi <= 400:
        parser.error('DPI must be between 72 and 400')
    root = Path(__file__).resolve().parents[1]
    filename = {'regelbuch': 'regelbuch-de-v2.pdf', 'quickstart': 'quickstart-de-v1.pdf'}[args.source]
    with fitz.open(root / 'assets' / filename) as doc:
        if not 1 <= args.page <= len(doc):
            parser.error(f'Page must be between 1 and {len(doc)}')
        page = doc[args.page - 1]
        clip = page.rect
        if args.crop:
            x0, y0, x1, y1 = args.crop
            if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
                parser.error('Crop must satisfy 0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1')
            clip = fitz.Rect(clip.x0 + x0 * clip.width, clip.y0 + y0 * clip.height,
                             clip.x0 + x1 * clip.width, clip.y0 + y1 * clip.height)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        pix = page.get_pixmap(dpi=args.dpi, clip=clip, alpha=False)
        pix.save(str(args.output))
        print(f'{args.output.resolve()} ({pix.width}x{pix.height}; {args.source}, PDF page {args.page})')


if __name__ == '__main__':
    main()
