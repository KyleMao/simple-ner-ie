import os.path as opath
from sys import path as spath
PROJECT_ROOT = opath.join(opath.dirname(__file__), '..')
spath.append(opath.join(PROJECT_ROOT, 'lib'))
from mitie import *


def train_ner(sents):
    num_threads = 4
    data_dir = opath.join(PROJECT_ROOT, 'data')
    trainer = ner_trainer(
        opath.join(data_dir, 'models/total_word_feature_extractor.dat'))
    for sent in sents:
        if sent.has_entity():
            sample = ner_training_instance(sent.tokens)
            for mention_range, mention_type in sent.entities.items():
                sample.add_entity(
                    xrange(mention_range[0], mention_range[1]), mention_type)
                trainer.add(sample)
    trainer.num_threads = num_threads
    recognizer = trainer.train()
    recognizer.save_to_disk(opath.join(data_dir, 'new_ner_model.dat'))

    return recognizer
