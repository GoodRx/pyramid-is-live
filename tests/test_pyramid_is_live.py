from pretend import call
from pretend import call_recorder
from pyramid import testing
from pyramid.request import apply_request_extensions
from pyramid.request import Request
import pytest

from pyramid_is_live import request_is_live_tween_factory


@pytest.fixture
def config():
    """Minimal Pyramid testing setup."""
    config = testing.setUp()
    config.include("pyramid_is_live")
    yield config
    testing.tearDown()


@pytest.fixture
def request_factory(config):
    """Factory for creating requests, using the registry from :func:`.config`."""

    def make_request(path="/", **kwargs):
        request = Request.blank(path, **kwargs)
        request.registry = config.registry
        apply_request_extensions(request)
        return request

    return make_request


def test_request_is_live(request_factory):
    request = request_factory()

    assert not request.is_live
    request.environ["LIVE_REQUEST"] = True
    assert request.is_live


def test_request_is_live_tween_factory(config, request_factory):
    # Arbitrary request handler
    handler = call_recorder(id)

    tween = request_is_live_tween_factory(handler, config.registry)
    request = request_factory()
    resp = tween(request)

    assert request.environ["LIVE_REQUEST"] == True

    # The tween returned the result of its handler
    assert handler.calls == [call(request)]
    assert resp == handler(request)
