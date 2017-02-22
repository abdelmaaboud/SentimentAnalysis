from ReviewsAnalyser import Analyser
from AspectExtractor import Aspect

import matplotlib.pyplot as plt
def draw_graph_(dict):
    aspects_names = []
    pos= []
    neg= []
    for item in dict:
        if dict[item]["pos"] == 0 and dict[item]["neg"]== 0:
            continue

        aspects_names.append(item)
        pos.append(dict[item]["pos"])
        neg.append(dict[item]["neg"])

    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = len(aspects_names)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, pos, bar_width,
                     alpha=opacity,
                     color='b',
                     label='pos')

    rects2 = plt.bar(index + bar_width, neg, bar_width,
                     alpha=opacity,
                     color='g',
                     label='neg')

    plt.xlabel('aspects')
    plt.ylabel('polarity')
    plt.title('polarity of aspects')
    plt.xticks(index + bar_width, aspects_names)
    plt.legend()

    plt.tight_layout()
    plt.show()



all_reviews = []
all_aspects=[]
file_name = "Nokia 6610.txt"
file = open(file_name)
for line in file :
    if "##" in line:
        sentences = line.split("##")
        for i in range(1,len(sentences)):
            all_reviews.append(sentences[i])


aspect = Aspect(all_reviews)
aspect_list_dictinary = aspect.extract_aspects()
aspect_list = list(aspect_list_dictinary.keys())
analyser = Analyser(all_reviews,aspect_list,aspect_list_dictinary)
output = analyser.analyse_reviews()
from ReviewsAnalyser import Analyser
from aspectExtractor import Aspect

import matplotlib.pyplot as plt
def draw_graph_(dict):
    aspects_names = []
    pos= []
    neg= []
    for item in dict:
        if dict[item]["pos"] == 0 and dict[item]["neg"]== 0:
            continue

        aspects_names.append(item)
        pos.append(dict[item]["pos"])
        neg.append(dict[item]["neg"])

    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = len(aspects_names)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, pos, bar_width,
                     alpha=opacity,
                     color='b',
                     label='pos')

    rects2 = plt.bar(index + bar_width, neg, bar_width,
                     alpha=opacity,
                     color='g',
                     label='neg')

    plt.xlabel('aspects')
    plt.ylabel('polarity')
    plt.title('polarity of aspects')
    plt.xticks(index + bar_width, aspects_names)
    plt.legend()

    plt.tight_layout()
    plt.show()



all_reviews = []
all_aspects=[]
file_name = "Nokia 6610.txt"
file = open(file_name)
for line in file :
    if "##" in line:
        sentences = line.split("##")
        for i in range(1,len(sentences)):
            all_reviews.append(sentences[i])


aspect = Aspect(all_reviews)
aspect_list_dictinary = aspect.extract_aspects()
aspect_list = list(aspect_list_dictinary.keys())
analyser = Analyser(all_reviews,aspect_list,aspect_list_dictinary)
output = analyser.analyse_reviews()
print(output)
draw_graph_(output)(output)
draw_graph_(output)