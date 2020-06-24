
from sklearn.neighbors import LocalOutlierFactor
import pandas as pd
import numpy as np
import csv

def load_data():
    file_name = "" # .csv INPUT

    training_f = open(file_name, "r")
    training_csvReader = csv.reader(training_f)
     
    next(training_csvReader) # Remove First Row

    total_node = list(training_csvReader)
    for i in range(len(total_node)) :
        total_node[i].pop(0)
        
    total_node = np.array(total_node, dtype=np.float64)
    print(total_node)
    return total_node

# fit the model for outlier detection (default : n_neighbors=3, contamination=0.1)
clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
y_pred = clf.fit_predict(load_data())
X_scores = clf.negative_outlier_factor_
X_scores = np.array(X_scores, dtype=np.float64)
print(-X_scores)

df = pd.DataFrame(-X_scores)
df.to_csv('',index=False) # .csv OUPUT

