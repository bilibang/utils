#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import logging

dir_path = sys.argv[1]
for f in os.listdir(dir_path):
    children_path = dir_path + f
    if os.path.isfile(children_path):
        # 删除无用文件
        if f.startswith(".") and os.path.getsize(children_path) < 1024 * 1024:
            os.remove(children_path)
            logging.info("Delete: " + children_path)
            continue
        # 除了后缀外，字母大写
        os.rename(children_path,
                  os.path.splitext(children_path)[0].strip().upper() + os.path.splitext(children_path)[-1])
    else:
        logging.warning("Skip: " + children_path)
        continue
