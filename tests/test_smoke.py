from app import create_app

def test_health():
    app = create_app("testing")
    client = app.test_client()

    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json() == {"ok": True}