# -*- coding: utf-8 -*-

import os.path
import zipfile
import xml.etree.ElementTree as et

def get_office(filepath):
    root, ext = os.path.splitext(filepath)
    prefix = None
    
    if ext == '.pptx':
        prefix = 'ppt/slides/slide'
    elif ext == '.xlsx':
        prefix = 'xl/sharedStrings'
    elif ext == '.docx':
        prefix = 'word/document'
    
    if prefix is not None:
        xmls = []
        zf = None
        try:
            zf = zipfile.ZipFile(filepath, 'r')
            for name in zf.namelist():
                if name.startswith(prefix):
                    xmls.append(zf.read(name).decode('utf8'))
        finally:
            if zf is not None:
                zf.close()
        return xmls
    return None

get_office('分類.xlsx')

