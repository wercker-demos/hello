from webtest import TestApp

import hello


def test_functional_say_hello():
    """See if we get the default response back"""

    app = TestApp(hello.app)

    # Make a get request to our app
    resp = app.get('/')

    # test that the body of the response contains our default message
    resp.mustcontain("TEST MESSAGE")

    # Test that we got a successful HTTP response code
    assert resp.status == "200 OK"
