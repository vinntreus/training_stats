import pytest
from .setup_db import create_tables, add_test_users
from web.app import app as the_app, db as the_db, init_app


init_app(the_app, dict(
    DEBUG=True,
    TESTING=True,  # Propagate exceptions
    LOGIN_DISABLED=False,  # Enable @register_required
    MAIL_SUPPRESS_SEND=True,  # Disable Flask-Mail send
    SERVER_NAME='localhost',  # Enable url_for() without request context
    WTF_CSRF_ENABLED=False,  # Disable CSRF form validation,
    # SQLALCHEMY_ECHO=True,
))

# Setup an application context
# since the tests run outside of the webserver context
the_app.app_context().push()

# Setup db
create_tables()
add_test_users()


@pytest.fixture(scope='session')
def app():
    return the_app


@pytest.fixture(scope='session')
def db():
    return the_db
