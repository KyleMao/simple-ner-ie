import os
from os import path
from nose.tools import *
from ner_ie import extract_text


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_extract():
    print "I RAN!"
    raw_dir = path.abspath('data/Raw')
    raw_files = [f for f in os.listdir(raw_dir) if path.isfile(path.join(raw_dir, f))]
    raw_files.sort()
    for raw_file in raw_files:
        extract_text.extract_text(path.join(raw_dir, raw_file))
