import os
import pytest
import submarine


@pytest.fixture
def tmp_wkdir(tmpdir):
    initial_wkdir = os.getcwd()
    os.chdir(str(tmpdir))
    yield
    os.chdir(initial_wkdir)


@pytest.fixture
def reset_active_experiment():
    yield
    submarine.tracking.fluent._active_experiment_id = None
