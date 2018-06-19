"""
Add an ``is_live`` property to the request to differentiate between live
requests and scripts.
"""
from pyramid.tweens import INGRESS

__version__ = "0.1.0"


def request_is_live_tween_factory(handler, registry):
    """
    Tween that adds ``LIVE_REQUEST`` to the request's environment, used to
    determine ``request.is_live``.

    .. note::

        This should be added as close as possible to
        :data:`pyramid.tweens.INGRESS` so that ``request.is_live`` can be used
        in other tweens.
    """

    def request_is_live_tween(request):
        request.environ["LIVE_REQUEST"] = True
        return handler(request)

    return request_is_live_tween


def is_live_request(request):
    """
    Helper to differentiate between live requests and scripts.

    Requires :func:`~.request_is_live_tween_factory`.
    """
    return request.environ.get("LIVE_REQUEST", False)


def includeme(config):
    config.add_request_method(is_live_request, "is_live", property=True)
    config.add_tween("pyramid_is_live.request_is_live_tween_factory", under=INGRESS)
