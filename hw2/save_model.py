from gensim.models import word2vec

sentences = word2vec.Text8Corpus(r'gene/all_text.txt')
model = word2vec.Word2Vec(sentences, size=100,negative =5, min_count=2, window=5)
model.save('word2vec/Aword2vec.model')