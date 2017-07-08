def login(client):
    response = client.post(
        '/user/sign-in?next=/',
        follow_redirects=True,
        data=dict(
            username='test@test.com',
            password='Password1'
        )
    )
    return response


def test_navigating_to_startpage(app):
    client = app.test_client()
    login(client)
    response = client.get('/')
    assert response.status_code == 200
    assert b"<title>Training stats</title>" in response.data


def test_create_workout(app):
    client = app.test_client()
    login(client)
    response = client.post(
        '/workouts/new',
        data={
            'date': '2017-01-01'
        },
        follow_redirects=True,
    )
    assert b"2017-01-01" in response.data


def test_create_workout_with_exercises(app):
    client = app.test_client()
    login(client)
    response = client.post(
        '/workouts/new',
        data={
            'date': '2017-01-02',
            'exercises': """[
                {
                    "name": "marklyft",
                    "sets": [{"reps": 10, "weight": 2, "note": "easy"}]
                }
            ]""",
        },
        follow_redirects=True,
    )
    assert b"2017-01-02" in response.data
    assert b"marklyft" in response.data
    assert b"10" in response.data
    assert b"2" in response.data
    assert b"easy" in response.data
