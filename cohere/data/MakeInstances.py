import lxml.objectify
from collections import defaultdict

class Lexicon:
    def __init__(self):
        self.ider = defaultdict(lambda: 0)
        self.count = 1

    def __getitem__(self, word):
        return self.ider[word]

    def add(self, word):
        if word in self.ider:
            return self.ider[word]
        else:
            self.ider[word] = self.count
            self.count += 1
            return self.count - 1

def make_instance(i):
    sentences = open("/home/srush/Data/wikipedia/simple/docs/docs_%04d"%i)
    docs = []
    for i in range(1000):
        tree = lxml.objectify.parse(open("/home/srush/Data/wikipedia/simple/processed/docs_%04d.xml"%i))
        print i

        doc = tree.getroot().document
        lexicon = Lexicon()
        sents = [] 
        for sentence in doc.sentences.sentence:
            sent_tokens = []
            sparse_vec = set()
            for token in sentence.tokens.token:
                word = token.word
                sent_tokens.append(word)
                # v = lexicon.add(word)
                sparse_vec.add(u"Word:%s"%word)
            if not sentence.dependencies.find("dep"):
                 continue
            for dep in sentence.dependencies.dep:
                #print dep.get("type"),
                sparse_vec.add(u"Type:%s:%s"%(dep.dependent, dep.get("type")))

            if sent_tokens[-1] == "." and len(sent_tokens) > 8: 
                sents.append(sparse_vec)
        docs.append(sents)
    return docs

def vectorify(docs):
    lex = Lexicon()
    return [[{lex.add(element) for element in sent}
             for sent in doc]
            for doc in docs]





if __name__ == "__main__":
    docs = make_instance(0)
    print docs[0][0]
    vectors = vectorify(docs)
    for doc in vectors:
        for sent in doc:
            for element in sent:
                print element,
            print
        print
