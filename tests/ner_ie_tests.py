import os
from os import path
from nose.tools import *
from ner_ie import read_entity
from ner_ie.sentence_extractor import SentenceExtractor


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_extract_segment():
    print "I RAN!"
    raw_dir = path.abspath('data/Raw')
    anno_dir = path.abspath('data/Annotated')
    raw_files = [
        f for f in os.listdir(raw_dir) if path.isfile(path.join(raw_dir, f))]
    raw_files.sort()
    anno_files = [
        f for f in os.listdir(anno_dir) if path.isfile(path.join(anno_dir, f))]
    anno_files.sort()
    # sent_extractor = SentenceExtractor()
    # for raw_file in raw_files:
    #     sent_extractor.get_sentences(path.join(raw_dir, raw_file))
    for anno_file in anno_files:
        read_entity.read_entity(path.join(anno_dir, anno_file))
