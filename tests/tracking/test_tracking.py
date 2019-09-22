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

import submarine
from os import environ
from submarine.store.database.models import SqlMetric, SqlParam
from submarine.tracking import utils

JOB_NAME = "application_123456789"


def test_log_param(tracking_uri_mock):
    environ["SUBMARINE_JOB_NAME"] = JOB_NAME
    submarine.log_param("name_1", "a", "worker-1")

    tracking_uri = utils.get_tracking_uri()
    store = utils.get_sqlalchemy_store(tracking_uri)

    # Validate params
    with store.ManagedSessionMaker() as session:
        params = session \
            .query(SqlParam) \
            .options() \
            .filter(SqlParam.job_name == JOB_NAME).all()
        assert params[0].key == "name_1"
        assert params[0].value == "a"
        assert params[0].worker_index == "worker-1"
        assert params[0].job_name == JOB_NAME


def test_log_metric(tracking_uri_mock):
    environ["SUBMARINE_JOB_NAME"] = JOB_NAME
    submarine.log_metric("name_1", 5, "worker-1")
    submarine.log_metric("name_1", 6, "worker-2")

    tracking_uri = utils.get_tracking_uri()
    store = utils.get_sqlalchemy_store(tracking_uri)

    # Validate params
    with store.ManagedSessionMaker() as session:
        metrics = session \
            .query(SqlMetric) \
            .options() \
            .filter(SqlMetric.job_name == JOB_NAME).all()
        assert len(metrics) == 2
        assert metrics[0].key == "name_1"
        assert metrics[0].value == 5
        assert metrics[0].worker_index == "worker-1"
        assert metrics[0].job_name == JOB_NAME
        assert metrics[1].value == 6
        assert metrics[1].worker_index == "worker-2"
