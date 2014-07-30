from corenlp.pipeline import  files2dir

def preprocess(docs):

    annotators = ['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse']
    out_dir = "/home/srush/Data/wikipedia/simple/processed"
    files2dir(annotators=annotators,
              files=docs,
              out_dir=out_dir, 
              libver="3.4",
              libdir='/home/srush/Libs/stanford-corenlp-full-2014-06-16') 

def break_up(f):
    for l in f:
        if "<doc" in l:
            collect = ""
        elif "</doc" in l:
            yield collect
        else: collect += l


if __name__ == "__main__": 
    import os

    out = "/home/srush/Data/wikipedia/simple/docs/docs_%04d"
    f =  "/home/srush/Data/wikipedia/simple/AA/wiki_%02d"
    i = 0 
    docs = []
    for j in range(5):
        for doc in break_up(open(f%j)):
            print >>open(out%i, "w"), doc
            docs.append(out%i)
            i += 1
    preprocess(docs)
