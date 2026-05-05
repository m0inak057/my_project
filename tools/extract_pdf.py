import sys
def main():
    try:
        from pypdf import PdfReader
    except Exception as e:
        print('MISSING_PYPDF')
        raise
    if len(sys.argv) < 2:
        print('usage: python extract_pdf.py <path-to-pdf>')
        return
    path = sys.argv[1]
    reader = PdfReader(path)
    out = []
    for p in reader.pages:
        t = p.extract_text()
        if t:
            out.append(t)
    print('\n\n'.join(out))

if __name__ == '__main__':
    main()
