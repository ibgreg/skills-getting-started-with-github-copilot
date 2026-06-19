import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_activities():
    """Provide a stable copy of the in-memory activities data for each test."""
    original_activities = copy.deepcopy(activities)

    activities.clear()
    activities.update(copy.deepcopy(original_activities))

    yield activities

    activities.clear()
    activities.update(copy.deepcopy(original_activities))
