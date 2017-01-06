#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import re
import zipfile
import StringIO


data_dir = 'data'
def main():
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    response = urllib2.urlopen('https://u-go.net/gamerecords/')
    content = response.read()

    links = re.findall("https://.*?[.]zip", content)
    for link in links:
        extract(link)

def extract(link):
    print link
    response = urllib2.urlopen(link)
    content = response.read()
    for name, data in extract_zip(content):
        path = os.path.join(data_dir, name)
        ensure_dir_for(path)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write(data)

def ensure_dir_for(path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def extract_zip(input_zip):
    reader = StringIO.StringIO(input_zip)
    input_zip=zipfile.ZipFile(reader)
    for name in input_zip.namelist():
        yield name, input_zip.read(name)
    




main()
