import os
from os import path
from nose.tools import *
from ner_ie import prepare_ner_sentence
from ner_ie import read_entity
from ner_ie.sentence_extractor import SentenceExtractor
from ner_ie import train_ner


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_pipeline():
    print "I RAN!"
    raw_dir = path.abspath('data/Raw')
    anno_dir = path.abspath('data/Annotated')
    raw_files = [
        f for f in os.listdir(raw_dir) if path.isfile(path.join(raw_dir, f))]
    raw_files.sort()
    anno_files = [
        f for f in os.listdir(anno_dir) if path.isfile(path.join(anno_dir, f))]
    anno_files.sort()
    sent_extractor = SentenceExtractor()
    all_sents = []
    # for idx in range(len(raw_files)):
    for idx in [1]:
        raw_file = raw_files[idx]
        anno_file = anno_files[idx]
        sents = sent_extractor.get_sentences(path.join(raw_dir, raw_file))
        all_sents.extend(sents)
        mentions = read_entity.read_entity(path.join(anno_dir, anno_file))
        prepare_ner_sentence.prepare(sents, mentions)
    # print 'Start training!'
    # train_ner.train_ner(all_sents)
