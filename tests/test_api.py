from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_file():
    response = client.get("/read?path=/data/test.txt")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert "content" in response.json()
    else:
        assert "File not found" in response.text