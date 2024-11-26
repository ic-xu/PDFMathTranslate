import sys

from pdf2zh.pdf2zh import main

if __name__ == '__main__':
    pdf_path = '/Users/chenxu/workspace/python3/PDFMathTranslate/dataset/attention-is-all-you-need.pdf'
    sys.exit(main(["-i"]))