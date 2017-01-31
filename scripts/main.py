#!/usr/bin/env python
#########################
# AUTHOR: Brian Lai
# DATE: 1/14/2017
#########################

__author__ = 'brian.lai@protonmail.com'

from googleapiclient.discovery import build
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import os, sys, argparse


# API Key for google translate api
key=''

def translate(word, service, target_lang):
    translated_text = service.translations().list(
        source='en',
        target=target_lang,
        q=word
        ).execute()
    return translated_text['translations'][0]['translatedText']

def iterate_xml(file_name, service, target_lang):
    tree = ET.parse(file_name)
    translations = tree.getroot()

    for entry in translations:
        try:
            key = entry.find('key').text
            translated_key = translate(key, service, target_lang)
            xmlString=u'\n<'+target_lang+'>'+translated_key+u'</'+target_lang+'>\n'
            xmlString = xmlString.encode('utf-8')
            try:
                entry.append(ET.fromstring(xmlString))
            except:
                print(file_name, key, translated_key)
        except AttributeError as e:
            print(e, '\n')
            break
    tree.write(file_name, encoding="utf-8")

def main(service):
    parser = argparse.ArgumentParser(description='translates SocialFlow pages into different languages')
    parser.add_argument('--language', action="store", dest="language", default='')
    parser.add_argument('--directory', action="store", dest="directory", default='new_xml/')
    args = parser.parse_args()

    directory = args.directory
    target_lang = args.language
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filename = os.path.join(directory, filename)
            iterate_xml(filename, service, target_lang)
            print('*********************\n')
            print('Success: translated', filename, '\n')
            print('*********************\n')

if __name__ == '__main__':
    # Build a service object for interacting with the API.
    service = build('translate', 'v2', developerKey=key)
    main(service)
