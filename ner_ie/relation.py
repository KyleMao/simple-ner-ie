class Relation():
    """A class for binary relations between entities.

    Attributes:
        sent: A Sentence object containing the sentence involved in the
            relation.
        relation_type: A string containing the type of the relation.
        subtype: A string containing the subtype of the relation.
        arg1: A tuple indicating the first entity mention in this relation.
        arg2: A tuple indicating the second entity mention in this relation.
    """

    def __init__(self, sent, relation_elem):
        self.sent = sent
        self.relation_type = relation_elem.attrib['type']
        self.subtype = relation_elem.attrib['subtype']

        for arg in relation_elem.iter('arg'):
            if arg.attrib['number'] == '1':
                self.arg1 = sent.get_entity_range(
                    arg.attrib['entity_mention_id'])
            elif arg.attrib['number'] == '2':
                self.arg2 = sent.get_entity_range(
                    arg.attrib['entity_mention_id'])
