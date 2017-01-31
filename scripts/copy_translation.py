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
    source_file_name = os.path.join('new_xml/', file_name)
    target_file_name = os.path.join('xml/', file_name)
    source_tree = ET.parse(source_file_name)
    target_tree = ET.parse(target_file_name)
    source_entries = source_tree.getroot()
    target_entries = target_tree.getroot()

    for source_entry, target_entry in zip(source_entries, target_entries):
        try:
            if (target_entry.find(target_lang).text != source_entry.find(target_lang).text):
                print(target_entry.find(target_lang).text)
                print(source_entry.find(target_lang).text)
            target_entry.find(target_lang).text = source_entry.find(target_lang).text
        except AttributeError as e:
            print(e, '\n')
            break
    target_tree.write(target_file_name, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description='copies over language into another xml')
    parser.add_argument('--language', action="store", dest="language", default='')
    args = parser.parse_args()

    target_lang = args.language
    directory = 'xml'
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            iterate_xml(filename, target_lang)
            print('Success: copied over to ' + filename + '\n')

if __name__ == '__main__':
    main()
