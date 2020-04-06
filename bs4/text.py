#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os
from bs4 import BeautifulSoup


def extract_text(dir):
    filenames = sorted(os.listdir(dir))
    with open('mzd.md', 'w') as md_file:
        md_file.write('[TOC]\n')  # 目录
        for filename in filenames:
            content = ''
            if filename.endswith(".htm"):
                # HTML 中 charset=gb2312，但 encoding="gb2312" 时，总是有个别文件报错，
                # 改为 gb18030 后正常
                with open(os.path.join("mzd", filename), encoding="gb18030") as file:
                    bs = BeautifulSoup(file.read(), "html.parser")
                    content = '## ' + bs.td.get_text().lstrip()
            md_file.write(content)


if __name__ == '__main__':
    extract_text(sys.argv[1])
