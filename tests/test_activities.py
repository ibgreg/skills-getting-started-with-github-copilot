from fastapi.testclient import TestClient


def test_get_activities_returns_all_activity_data(client: TestClient, sample_activities):
    # Arrange
    expected_activity_names = sample_activities.keys()

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == sample_activities
    assert set(response.json().keys()) == set(expected_activity_names)


def test_root_redirects_to_the_static_frontend(client: TestClient):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location
