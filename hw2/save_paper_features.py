import re
import numpy as np
from gensim.models import word2vec
from load_save_data import load_json, dump_data


def save_relation(name_pubs_raw, name):  # 保存论文的各种feature
    name_pubs_raw = load_json('genename', name_pubs_raw)
    ## trained by all text in the datasets. Training code is in the cells of "train word2vec"
    save_model_name = "word2vec/Aword2vec.model"
    model_w = word2vec.Word2Vec.load(save_model_name)

    r = '[!“”"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—～’]+'
    stopword = ['at', 'based', 'in', 'of', 'for', 'on', 'and', 'to', 'an', 'using', 'with', 'the', 'by', 'we', 'be',
                'is', 'are', 'can']
    stopword1 = ['university', 'univ', 'china', 'department', 'dept', 'laboratory', 'lab', 'school', 'al', 'et',
                 'institute', 'inst', 'college', 'chinese', 'beijing', 'journal', 'science', 'international']

    f1 = open('gene/paper_author.txt', 'w', encoding='utf-8')
    f2 = open('gene/paper_conf.txt', 'w', encoding='utf-8')
    f3 = open('gene/paper_word.txt', 'w', encoding='utf-8')
    f4 = open('gene/paper_org.txt', 'w', encoding='utf-8')

    taken = name.split("_")
    name = taken[0] + taken[1]
    name_reverse = taken[1] + taken[0]
    if len(taken) > 2:
        name = taken[0] + taken[1] + taken[2]
        name_reverse = taken[2] + taken[0] + taken[1]

    authorname_dict = {}
    ptext_emb = {}

    tcp = set()
    for i, pid in enumerate(name_pubs_raw):

        pub = name_pubs_raw[pid]

        # save authors
        org = ""
        for author in pub["authors"]:
            authorname = re.sub(r, '', author["name"]).lower()
            taken = authorname.split(" ")
            if len(taken) == 2:  ##检测目前作者名是否在作者词典中
                authorname = taken[0] + taken[1]
                authorname_reverse = taken[1] + taken[0]

                if authorname not in authorname_dict:
                    if authorname_reverse not in authorname_dict:
                        authorname_dict[authorname] = 1
                    else:
                        authorname = authorname_reverse
            else:
                authorname = authorname.replace(" ", "")

            if authorname != name and authorname != name_reverse:
                f1.write(pid + '\t' + authorname + '\n')

            else:
                if "org" in author:
                    org = author["org"]

        # save org 待消歧作者的机构名
        pstr = org.strip()
        pstr = pstr.lower()  # 小写
        pstr = re.sub(r, ' ', pstr)  # 去除符号
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()  # 去除多余空格
        pstr = pstr.split(' ')
        pstr = [word for word in pstr if len(word) > 1]
        pstr = [word for word in pstr if word not in stopword1]
        pstr = [word for word in pstr if word not in stopword]
        pstr = set(pstr)
        for word in pstr:
            f4.write(pid + '\t' + word + '\n')

        # save venue
        pstr = pub["venue"].strip()
        pstr = pstr.lower()
        pstr = re.sub(r, ' ', pstr)
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
        pstr = pstr.split(' ')
        pstr = [word for word in pstr if len(word) > 1]
        pstr = [word for word in pstr if word not in stopword1]
        pstr = [word for word in pstr if word not in stopword]
        for word in pstr:
            f2.write(pid + '\t' + word + '\n')
        if len(pstr) == 0:
            f2.write(pid + '\t' + 'null' + '\n')

        # save text
        pstr = ""
        keyword = ""
        if "keywords" in pub:
            for word in pub["keywords"]:
                keyword = keyword + word + " "
        pstr = pstr + pub["title"]
        pstr = pstr.strip()
        pstr = pstr.lower()
        pstr = re.sub(r, ' ', pstr)
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
        pstr = pstr.split(' ')
        pstr = [word for word in pstr if len(word) > 1]
        pstr = [word for word in pstr if word not in stopword]
        for word in pstr:
            f3.write(pid + '\t' + word + '\n')

        # save all words' embedding
        pstr = keyword + " " + pub["title"] + " " + pub["venue"] + " " + org
        if "year" in pub:
            pstr = pstr + " " + str(pub["year"])
        pstr = pstr.strip()
        pstr = pstr.lower()
        pstr = re.sub(r, ' ', pstr)
        pstr = re.sub(r'\s{2,}', ' ', pstr).strip()
        pstr = pstr.split(' ')
        pstr = [word for word in pstr if len(word) > 2]
        pstr = [word for word in pstr if word not in stopword]
        pstr = [word for word in pstr if word not in stopword1]

        words_vec = []
        for word in pstr:
            if (word in model_w):
                words_vec.append(model_w[word])
        if len(words_vec) < 1:
            words_vec.append(np.zeros(100))
            tcp.add(i)
            # print ('outlier:',pid,pstr)
        ptext_emb[pid] = np.mean(words_vec, 0)

    #  ptext_emb: key is paper id, and the value is the paper's text embedding
    dump_data(ptext_emb, 'gene', 'ptext_emb.pkl')
    # the paper index that lack text information
    dump_data(tcp, 'gene', 'tcp.pkl')

    f1.close()
    f2.close()
    f3.close()
    f4.close()