from textblob import TextBlob
import nltk
class Analyser:
    def __init__(self, reviews_list,aspects_list,aspect_list_dictionary):
        self.reviews = reviews_list
        self.aspects=aspects_list
        self.aspects_list_dictionary=aspect_list_dictionary
        print(aspects_list)
        self.dict = {}


    def analyse_reviews(self):
        for i in self.aspects:
            self.dict[i] = {"pos": 0, "neg": 0}
        for word in self.reviews:
            #w = TextBlob(review)
            #word = str(w.correct())
            word_tokonize = nltk.word_tokenize(word)
            Filterd_Sentence = []
            s = ""
            i=0
            while i < len(word_tokonize):
                for j in range(len(self.aspects)):
                    if word_tokonize[i] == self.aspects[j]:
                        s = s + word_tokonize[i] + ' '
                textblob = TextBlob(word_tokonize[i])
                if word_tokonize[i] == 'not' or word_tokonize[i] == r"n't":
                    count_not = 1
                    for k in range(i + 1, len(word_tokonize)):
                        if word_tokonize[k] == word_tokonize[i]:
                            count_not += 1
                            i=k
                            continue
                        textblob = TextBlob(word_tokonize[k])
                        if textblob.sentiment.polarity != 0 and count_not % 2 != 0:
                            s = s + word_tokonize[i] + ' ' + word_tokonize[k] + ' '
                            i = k + 1
                            break
                        elif textblob.sentiment.polarity != 0 and count_not % 2 == 0:
                            s = s + word_tokonize[k] + ' '
                            i = k + 1
                            break
                        else:
                            i = k
                            break
                    continue
                if word_tokonize[i] == 'but' or word_tokonize[i] == ',' or word_tokonize[i] == 'and':
                    Filterd_Sentence.append(s)
                    s = ""
                elif textblob.sentiment.polarity != 0:
                    s = s + word_tokonize[i] + ' '

                i += 1

            if s != '':
                Filterd_Sentence.append(s)


            for i in Filterd_Sentence:
                #if ("not" in i) or (r"n't" in i) :
                    #print(i)
                for j in self.aspects:
                    if j in i:
                        blob = TextBlob(i)
                        score = blob.sentiment.polarity
                        if score > 0:
                            self.dict[j]["pos"] += 1
                        elif score < 0:
                            self.dict[j]["neg"] += 1
                        break
                for a in range(len(self.aspects)):
                    tmp_list = self.aspects_list_dictionary[self.aspects[a]]
                    for j in tmp_list:
                        if j in i:
                            blob = TextBlob(i)
                            score = blob.sentiment.polarity
                            if score > 0:
                                self.dict[self.aspects[a]]["pos"] += 1
                            elif score < 0:
                                self.dict[self.aspects[a]]["neg"] += 1
                            break

        for j in self.aspects:
            total = self.dict[j]["pos"] + self.dict[j]["neg"]
            if (total != 0):
                pos_per = round((self.dict[j]["pos"] / total) * 100, 2)
                neg_per =  round((self.dict[j]["neg"] / total) * 100, 2)
                print(j + " pos is " + str(pos_per) + "%" + " neg is " + str(neg_per) + '%')
        return self.dict