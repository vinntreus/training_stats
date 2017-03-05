def test_web(app):
    client = app.test_client()
    response = client.post(
        '/user/sign-in?next=/',
        follow_redirects=True,
        data=dict(
            username='test@test.com',
            password='Password1'
        )
    )
    response = client.get('/')
    assert response.status_code == 200
    assert b"<title>Training stats</title>" in response.data
