# importing Libraries
import pandas as pd
import numpy as np
from apyori import apriori

# reading csv file into pandas dataframe
data = pd.read_csv("Transactions.csv", header=None)
print(data.shape)
print(data.head())

# creating transactions list of list from dataframe
Transactions = []
for i in range(1, data.shape[0]):
    Transactions.append([str(data.values[i, j]) for j in range(0, data.shape[1])])

# applying the apriori algorithm where support = 0.0045, confidence = 0.2, length = 2, lift = 3
association_rules = apriori(Transactions, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print("There are {} Relation derived.".format(len(association_results)))

for i in range(0, len(association_results)):
    print(association_results[i][0])

for item in association_results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    # second index of the inner list
    print("Support: " + str(item[1]))

    # third index of the list located at 0th
    # of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("--------------------------------------------")
