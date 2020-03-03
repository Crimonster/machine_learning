import re
from demo.utils import load_json

pubs_raw = load_json("train", "train_pub.json")
pubs_raw1 = load_json("sna_data", "sna_valid_pub.json")
r = '[!“”"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—～’]+'
f1 = open('gene/all_text.txt', 'w', encoding='utf-8')

def write_vec_in_file(fw, fo):
    """
    fw: 要写入的文件
    fo: 读取的源文件，为json格式
    """
    for i, pid in enumerate(fo):
        pub = fo[pid]

        for author in pub["authors"]:
            if "org" in author:
                org = author["org"]
                pstr = org.strip()
                pstr = pstr.lower()
                pstr = re.sub(r, ' ', pstr)
                pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
                fw.write(pstr + '\n')

        title = pub["title"]
        pstr = title.strip()
        pstr = pstr.lower()
        pstr = re.sub(r, ' ', pstr)
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
        fw.write(pstr + '\n')

        if "abstract" in pub and type(pub["abstract"]) is str:
            abstract = pub["abstract"]
            pstr = abstract.strip()
            pstr = pstr.lower()
            pstr = re.sub(r, ' ', pstr)
            pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
            fw.write(pstr + '\n')

        venue = pub["venue"]
        pstr = venue.strip()
        pstr = pstr.lower()
        pstr = re.sub(r, ' ', pstr)
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
        fw.write(pstr + '\n')

write_vec_in_file(f1,pubs_raw)
write_vec_in_file(f1,pubs_raw1)

f1.close()

from gensim.models import word2vec

sentences = word2vec.Text8Corpus(r'gene/all_text.txt')
model = word2vec.Word2Vec(sentences, size=100,negative =5, min_count=2, window=5)
model.save('word2vec/Aword2vec.model')