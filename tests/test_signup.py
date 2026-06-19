from fastapi.testclient import TestClient


def test_signup_for_activity_adds_a_new_participant(
    client: TestClient, sample_activities
):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {email} for {activity_name}"
    }
    assert email in sample_activities[activity_name]["participants"]


def test_signup_for_activity_rejects_duplicate_email(
    client: TestClient, sample_activities
):
    # Arrange
    activity_name = "Chess Club"
    email = sample_activities[activity_name]["participants"][0]

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}


def test_signup_for_activity_rejects_unknown_activity(client: TestClient):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_for_activity_removes_a_participant(
    client: TestClient, sample_activities
):
    # Arrange
    activity_name = "Chess Club"
    email = sample_activities[activity_name]["participants"][0]

    # Act
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Removed {email} from {activity_name}"
    }
    assert email not in sample_activities[activity_name]["participants"]


def test_unregister_for_activity_rejects_unknown_participant(
    client: TestClient, sample_activities
):
    # Arrange
    activity_name = "Chess Club"
    email = "missing@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}
