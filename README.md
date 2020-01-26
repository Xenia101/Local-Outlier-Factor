# Local-Outlier-Factor (LOF)

<p align=center>
  <img width="50%" src="https://github.com/Xenia101/Local-Outlier-Factor/blob/master/img/1.png?raw=true">
</p>

Local Outlier Factor Score 도출

### LOF 란?
>In anomaly detection, the local outlier factor (LOF) is an algorithm proposed by Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng and Jörg Sander in 2000 for finding anomalous data points by measuring the local deviation of a given data point with respect to its neighbours.
[WIKIPEDIA](https://en.wikipedia.org/wiki/Local_outlier_factor)

## EXAMPLE
```python
from sklearn.neighbors import LocalOutlierFactor
import numpy as np

clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
clf.fit_predict(load_data())
X_scores = clf.negative_outlier_factor_

X_scores # X_scores is a negative number
-X_scores # print positive number
```

## 설치 방법
- 실행 환경 (테스트 환경)
  - Windows 10 or Ubuntu Linux
  - Python3.x

## 사용 방법

- Input : ```example_of_input.csv```

  `python3 LocalOutlierFactor.py`

- Output : ```example_of_output.csv``` with LOF scores
