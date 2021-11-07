__author__ = "joe"


def ddr_neighbors(dictionary_terms, model, n=2):

    # fields = dictionary_terms.keys()
    # ddr_neighbors_dic = {el: [] for el in fields}
    ddr_neighbors_dic = dict()

    for k in dictionary_terms:
        print("Querying nearest neighbors for {0}".format(k))
        sim = model.most_similar(dictionary_terms[k], topn=n)

        for word in sim:
            ddr_neighbors_dic.setdefault(k, []).append(word[0])

    print("finished")
    return ddr_neighbors_dic
