from  ReviewsAnalyser import Analyser
all_reviews = []
all_aspects=[]
file = open("Nokia 6610.txt")
for line in file :
    if "##" in line:
        sentences = line.split("##")
        for i in range(1,len(sentences)):
            all_reviews.append(sentences[i])

file2 = open("Aspects.txt")
aspects = file2.read()
analyser  = Analyser(reviews_list=all_reviews,aspects_list=all_aspects)
output = analyser.analyse_reviews()
for i in output:
    print(i)
