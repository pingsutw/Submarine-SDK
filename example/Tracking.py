# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from os import environ
from sklearn.linear_model import LogisticRegression
import submarine


if __name__ == "__main__":
    # note: SUBMARINE_JOB_NAME should be set by submarine submitter
    environ["SUBMARINE_JOB_NAME"] = "application_1234"
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression(solver='liblinear', max_iter=100)
    submarine.log_param("max_iter", 100, "worker-1")
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score: %s" % score)
    submarine.log_metric("score", score, "worker-1")

