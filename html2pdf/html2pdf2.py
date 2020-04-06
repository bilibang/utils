#!/usr/bin/env python3
from PyPDF2 import PdfFileReader, PdfFileMerger


import os
'''
毛泽东选集 HTML2PDF
来源：http://www.dodobook.com/index.php?id=books/maozedongxuanji/000
异常处理方式：PyPDF2.utils.PdfReadError: Unexpected destination '/__WKANCHOR_2'
https://blog.csdn.net/xp5xp6/article/details/78435442
'''

limit = 388
url = 'http://www.dodobook.com/index.php?id=books/maozedongxuanji/'

for i in range(0, limit):
    urls = '{}{:0>3} '.format(url, i)
    cmd = 'wkhtmltopdf --minimum-font-size 25 --margin-left 0 --margin-right 0 \
        --no-background {} {}{:0>3}.pdf'.format(urls, i)
    os.system(cmd)


merger = PdfFileMerger()
filenames = sorted(os.listdir('.'))
i = 0
for filename in filenames:
    if filename.endswith(".pdf"):
        with open(filename, 'rb') as f:
            pdfReader = PdfFileReader(f)
            pdf_title = pdfReader.getDocumentInfo().title
            pdf_title = pdf_title.split('（')[0]
            bookmark = '{:0>3} {}'.format(i, pdf_title)
            merger.append(pdfReader, bookmark=bookmark, import_bookmarks=True)
            i = i+1
merger.write("all.pdf")
merger.close()
