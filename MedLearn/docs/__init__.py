

import os

docpath = os.path.dirname( __file__)

def getDoc(doc_name):
    #docfile = os.path.join(mypath,'docs/common_e_CorrStat.md')
    docfile = os.path.join(docpath, doc_name)
    with open(docfile) as f:
        doc = f.read()
    return doc