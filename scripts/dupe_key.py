#!/usr/bin/env python
#########################
# AUTHOR: Brian Lai
# DATE: 1/14/2017
#########################

__author__ = 'brian.lai@protonmail.com'

import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import os, sys, argparse

def iterate_xml(file_name, target_lang):
    tree = ET.parse(file_name)
    translations = tree.getroot()

    for entry in translations:
        try:
            keys = entry.findall(target_lang)
            if len(keys) > 1:
                entry.remove(keys[1])
        except AttributeError as e:
            print(e, '\n')
            break
    tree.write(file_name, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description='translates SocialFlow pages into different languages')
    parser.add_argument('--language', action="store", dest="language", default='')
    parser.add_argument('--directory', action="store", dest="directory", default='new_xml/')
    args = parser.parse_args()

    directory = args.directory
    target_lang = args.language
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filename = os.path.join(directory, filename)
            iterate_xml(filename, target_lang)
            print('*********************\n')
            print('Success: removed dupe keys from ', filename, '\n')
            print('*********************\n')

if __name__ == '__main__':
    main()
