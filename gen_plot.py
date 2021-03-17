import matplotlib.pyplot as plt
import numpy as np

data = np.fromregex('poll.csv', r'(\d+),"(.+)",(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)', np.object)

boxes = ["strongly\nagree", "agree", "neither agree\nor disagree", "disagree", "strongly\ndisagree", "abstain"]
for p in data:
    id = p[0]
    title = p[1]
    total = p[2]
    single_data = p[3:].astype(np.int)
    plt.bar([0,1,2,3,4,5], single_data, tick_label=boxes)
    plt.title("Q" +  str(id) + ": " + title + "\nReponses: " + str(total), wrap=True)
    plt.subplots_adjust(top=0.8)
    plt.savefig("plots/" + str(id))
    plt.close()
