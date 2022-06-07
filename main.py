import cosin_sim as cm
import UnionText as tt
import textPro
from textblob import TextBlob

print('choice your dataset .. ')
filename = textPro.choiceData()
n = textPro.numDoc(filename)
#print(filename)
print("doc ..")
doc = textPro.Documents(filename)
print(len(doc))

print("text processing ..")
text = textPro.text_pr(doc)
print(len(text))

print('union ..')

temp = tt.temp(text, n)
print(temp)
print(len(temp))


print('indexing ..')
index = tt.comparList(text, temp)

print('vector ... ')

vectors = []
for d in doc:
    vector = cm.text_to_vector(d)
    vectors.append(vector)

query = input("Search ...")
q = cm.text_to_vector(query)
query = textPro.qr_test_pr(query)
autocorrect = textPro.autoCorrect(query)
print(autocorrect)
#qu = textPro.listToString(query) #not work with that !
#autocorrect = TextBlob(qu) #qu should be string.
#result = autocorrect.correct()
#print(result)

print(q)
cosin_ = {}
for v in vectors:
    cosine = cm.get_cosine(v, q)
    cosin_[vectors.index(v)] = cosine
print('cosine similarity .. ')
print(cosin_)
print('sorting ..')
sort = tt.dictionairy(cosin_)
print(sort)
print(sort[0])
cos = tt.tfidf_vectorizer(doc, q)
#print(cos)
print('find documents .. ')
documents = tt.matching(query, index)
print(documents)
all = tt.find_doc(documents, sort)
print(all)
tt.print_doc(doc, all)
