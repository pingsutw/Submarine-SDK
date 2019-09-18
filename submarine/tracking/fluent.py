"""
Internal module implementing the fluent API, allowing management of an active
Submarine run. This module is exposed to users at the top-level :py:mod:`submarine` module.
"""
from __future__ import print_function
from submarine.tracking.client import SubmarineClient

import time
import logging
import random
import string

_RUN_ID_ENV_VAR = "SUBMARINE_RUN_ID"
_active_run_stack = []

_logger = logging.getLogger(__name__)


# Todo need to support unique run_id or change to submarine-job name
def random_string(stringLength=30):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def log_param(key, value, worker_index):
    """
    Log a parameter under the current run, creating a run if necessary.
    :param key: Parameter name (string)
    :param value: Parameter value (string, but will be string-ified if not)
    :param worker_index
    """
    run_id = random_string()
    SubmarineClient().log_param(run_id, key, value, worker_index)


def log_metric(key, value, worker_index, step=None):
    """
    Log a metric under the current run, creating a run if necessary.
    :param key: Metric name (string).
    :param value: Metric value (float). Note that some special values such as +/- Infinity may be
                  replaced by other values depending on the store. For example, sFor example, the
                  SQLAlchemy store replaces +/- Inf with max / min float values.
    :param worker_index: Metric worker_index (string).
    :param step: Metric step (int). Defaults to zero if unspecified.
    """
    run_id = random_string()
    SubmarineClient().log_metric(
        run_id, key, value, worker_index, int(time.time() * 1000), step or 0)
