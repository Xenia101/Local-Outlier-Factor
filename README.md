# Local-Outlier-Factor (LOF)

<p align=center>
  <img width="50%" src="https://github.com/Xenia101/Local-Outlier-Factor/blob/master/img/1.png?raw=true">
</p>

Deriving the Local Outlier Factor Scores

### LOF 란?
>In anomaly detection, the local outlier factor (LOF) is an algorithm proposed by Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng and Jörg Sander in 2000 for finding anomalous data points by measuring the local deviation of a given data point with respect to its neighbours.
[WIKIPEDIA](https://en.wikipedia.org/wiki/Local_outlier_factor)

## Example
```python
from sklearn.neighbors import LocalOutlierFactor
import numpy as np

clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
clf.fit_predict(load_data())
X_scores = clf.negative_outlier_factor_

X_scores  # X_scores is a negative number
-X_scores # print a positive number
```

## Execution / Test Environment
- Windows 10 or Ubuntu Linux
- Python **3.6**

## Usage

- Input : ```example_of_input.csv```

  `python3 LocalOutlierFactor.py`

- Output : ```example_of_output.csv``` with *LOF scores*
