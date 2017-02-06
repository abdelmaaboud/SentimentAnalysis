import nltk
class Analyser:
    chunkgram = r"""NP:{<NN>+<VBZ>+<JJ>}
                         {<VBP>+<DT>+<NN.?>}
                         {<VBP>+<NN.?>}
    """
    def __init__(self, reviews_list,aspects_list):
        self.reviews = reviews_list
        self.aspects=aspects_list
        self.chuncked = []
    def chunk_reviews(self):
        for review in self.reviews:
            token = nltk.word_tokenize(review)
            tagged = nltk.pos_tag(token)
            chunkparser = nltk.RegexpParser(self.chunkgram)
            self.chuncked.append(chunkparser.parse(tagged))
        return self.chuncked
    def analyse_reviews(self):
        # call all functions to analyse reviews
        # return the output
        chunked = self.chunk_reviews()
        # we will add functions when complete algorithm implementation
        return chunked


