import cosin_sim as cm
import UnionText as tt
import textPro as tp

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


#print('choice your dataset .. ')
print("doc ..")
doc = tp.Documents()
print(len(doc))

print("text processing ..")
text = tp.text_pr(doc)
print(len(text))

print('union ..')
temp = tt.temp(text, 1460)
print(temp)
print(len(temp))


print('indexing ..')
index = tt.comparList(text, temp)

root = tk.Tk()
root.title("YOUR SEARCH ENGIN ")
root.geometry('600x500')
root.resizable(False, False)

frame = ttk.Frame(root)

options = {'padx': 30, 'pady': 50}

query_label = ttk.Label(frame, text='Enter Your Query')
query_label.grid(column=0, row=0, sticky='W', **options)

query = tk.StringVar()
query_entry = ttk.Entry(frame, textvariable=query)
query_entry.grid(column=1, row=1, **options)
query_entry.focus()

vectors = []
for d in doc:
    vector = cm.text_to_vector(d)
    vectors.append(vector)

def search_button_clicked():
    """  Handle convert button click event
    """
    try:
        #return the document after the matching
        qr = query.get()
        qrr = cm.text_to_vector(qr)
        qr = tp.qr_test_pr(qr)
        autocorrect = tp.autoCorrect(qr)
        cosin_ = {}
        for v in vectors:
            cosine = cm.get_cosine(v, qrr)
            cosin_[vectors.index(v)] = cosine
        sort = tt.dictionairy(cosin_)
        cos = tt.tfidf_vectorizer(doc, qr)
        documents = tt.matching(query, index)
        all = tt.find_doc(documents, sort)
        result = tt.print_doc(doc, all)
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

convert_button = ttk.Button(frame, text='SEARCH')
convert_button.grid(column=0, row=2, sticky='W', **options)
convert_button.configure(command=search_button_clicked)


result_label = ttk.Label(frame)
result_label.grid(row=8, columnspan=10, **options)

frame.grid(padx=10, pady=50)

root.mainloop()
