from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
	resp = client.get("/")
	assert resp.status_code == 200
	data = resp.json()
	assert data["name"] == "devops-fastapi-app"
	assert "version" in data
	assert data["health_url"] == "/health"


def test_health():
	resp = client.get("/health")
	assert resp.status_code == 200
	assert resp.json() == {"status": "ok"}


def test_ping():
	resp = client.get("/ping")
	assert resp.status_code == 200
	assert resp.json() == {"message": "pong"}