import numpy as np
from sklearn.linear_model import LogisticRegression
import submarine
import random

if __name__ == "__main__":
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression(solver='liblinear', max_iter=100)
    submarine.log_param("max_iter", 100, "worker-1")
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score: %s" % score)
    submarine.log_metric("score", score, "worker-1")

