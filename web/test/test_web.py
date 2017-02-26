from web.app import app

def test_web():
    client = app.test_client()
    result = client.get('/')
    assert result.status_code == 200
    assert b"<title>Training stats</title>" in result.data
