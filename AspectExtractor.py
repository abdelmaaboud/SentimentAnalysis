import nltk
from nltk.corpus import wordnet
import inflect

inflect = inflect.engine()


class Aspect:
    #Aspect_list=list()

    def __init__(self, reviews):
        self.reviews = reviews

    def plural(self,l):
        d = dict()
        for i in range(0, len(l)):
            for j in range(1, len(l)):

                if l[i] == inflect.plural(l[j]):
                    if not (l[i] in d) or (l[j] in d ):
                        d[l[i]] = [l[j]]
                        break
        return d
    def filter_nouns(self,all_nouns):
        d=dict()
        Aspect_list_Filterd=[]
        for i in range(len(all_nouns)):
            d[all_nouns[i]]=0
        for j in range(len(all_nouns)):
           if all_nouns[j] in d:
              d[all_nouns[j]] += 1
              if d[all_nouns[j]] >= 15:
                  if all_nouns[j] not in Aspect_list_Filterd:
                        Aspect_list_Filterd.append(all_nouns[j])

        print(Aspect_list_Filterd)
        return Aspect_list_Filterd

    def extract_aspects(self):
        #d=dict()
        #t=tuple()
        all_nouns=[]
        for w in self.reviews:
           tokens=nltk.word_tokenize(w)
           tokens_Filterd=nltk.pos_tag(tokens)
           for i in range(len(tokens_Filterd)):
               t=tokens_Filterd[i]
               if (t[1]=="NN" or t[1]=="NNS") and t[0]!="i":
                   all_nouns.append(t[0])
        Aspect_list_Filterd=self.filter_nouns(all_nouns)

        l = list()
        l2 = list()
        d2 = dict()
        cnt = 0
        for i in range(len(Aspect_list_Filterd)):
            l.append(inflect.plural(Aspect_list_Filterd[i]))

        for i in range(len(Aspect_list_Filterd)):

            if Aspect_list_Filterd[i] in l:
                l2.append(Aspect_list_Filterd[i])

        for i in range(len(l2)):
            Aspect_list_Filterd.remove(l2[i])

        d_aspects = dict()
        for i in range(len(Aspect_list_Filterd)):
            d_aspects[Aspect_list_Filterd[i]] = []

        d = self.plural(l2)
        tmp = list()
        for i in range(len(tmp)):
            d_aspects[tmp[i]] = d[tmp[i]]

        return d_aspects