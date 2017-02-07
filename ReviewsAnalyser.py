import nltk
class Analyser:
    chunkgram = r"""NP:{<NN>+<VBZ>+<JJ>}
                         {<VBP>+<DT>+<NN.?>}
                         {<VBP>+<NN.?>}
    """
    def __init__(self, reviews_list,aspects_list):
        self.reviews = reviews_list
        self.aspects=aspects_list
        self.chunked_noun_phrases = []
        self.aspect_dictionary = dict()
    def get_noun_phrases(self):
        for review in self.reviews:
            token = nltk.word_tokenize(review)
            tagged = nltk.pos_tag(token)
            chunkparser = nltk.RegexpParser(self.chunkgram)
            self.chunked_noun_phrases.append(chunkparser.parse(tagged))
    def evaluate_polarity(self):
        # we will implement this function
        # use noun phrases as input  and return aspect dictionary
        print("dummy")


    def analyse_reviews(self):
        # call all functions to analyse reviews
        # return the output
        self.get_noun_phrases()
        self.evaluate_polarity()
        # we will add functions when complete algorithm implementation
        return self.aspect_dictionary


