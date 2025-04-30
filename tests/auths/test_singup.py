import pytest
from starlette.testclient import TestClient

from src.api.auths.singup import router
from src.auth.utils import verify_password
from src.model import User, UserRole

client = TestClient(router)

@pytest.fixture
def test_register(db):
    register_data = {
        "username": "testuser",
        "password": "Test",
        "role": User.role.value
    }

    response = client.post("/signup", json=register_data)

    assert response.status_code == 200
    data = response.json()
    assert data["message"] =="User register successfully"

    user = db.query(User).filter(User.username==register_data["username"]).first()

    assert user is not None
    assert user.username == register_data["username"]
    assert verify_password(register_data["password"], user.hashed_password)


def test_register_existing_user(db):
    user = User(username="existinguser", hashed_password= "hashedpassword", role=UserRole.value)
    db.add(user)
    db.commit()

    register_data = {
        "username": "existinguser",
        "password": "NewPass123",
        "role": UserRole.teacher.value
    }

    response = client.post("/signup", json= register_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Username already taken"